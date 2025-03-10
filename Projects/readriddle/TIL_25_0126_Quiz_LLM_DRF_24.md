# 챗봇 응답 비동기 처리 테스트

## 설정

### Celery 설정
- `Celery` 및 `Redis`를 설치
- `celery.py` 작성

```python
from __future__ import absolute_import
import os
from celery import Celery

# Django 설정 모듈 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

# Django 설정을 Celery에 로드
app.config_from_object("django.conf:settings", namespace="CELERY")

# 자동으로 task 모듈 로드
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

### Redis, Celery 설정

```python
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
```

## Celery 작업 정의
- 비동기 작업으로 실행될 함수 `@shared_task` 사용하여 정의

```python
from celery import shared_task

@shared_task
def generate_response(chat_history_id, user_input):
    # ChatHistory 로드
    chat_history = ChatHistory.objects.get(id=chat_history_id)
    memory = chat_history.conversation

    # LLM 작업 처리
    response = llm.process(user_input, memory)

    # 결과 반환
    return {"response": response, "summary_title": "요약된 제목"}
```

## API 생성

### 작업 요청

```python
from celery.result import AsyncResult
from .tasks import generate_response

class ChatView(APIView):
    def post(self, request, chat_id=False):
        user = request.user
        user_input = request.data["user_input"]

        # ChatHistory 생성/조회
        chat_history, created = ChatHistory.objects.get_or_create(
            user=user, defaults={"conversation": [], "content_info": {}}
        )

        # 비동기 작업 생성
        task = generate_response.delay(chat_history.id, user_input)

        return Response(
            {"task_id": task.id, "message": "응답을 생성 중입니다. 잠시만 기다려 주세요."},
            status=status.HTTP_202_ACCEPTED,
        )
```


### 작업 상태 확인
- `ID`를 통해 상태를 확인 : 풀링 방식으로 일정 시간마다 확인 요청
- 작업 완료 시 결과 데이터를 포함하여 응답

```python
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        if result.state == "PENDING":
            return Response({"status": "진행 중", "result": None}, status=status.HTTP_200_OK)
        elif result.state == "SUCCESS":
            return Response({"status": "완료", "result": result.result}, status=status.HTTP_200_OK)
        elif result.state == "FAILURE":
            return Response({"status": "실패", "result": str(result.info)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"status": result.state}, status=status.HTTP_200_OK)
```

