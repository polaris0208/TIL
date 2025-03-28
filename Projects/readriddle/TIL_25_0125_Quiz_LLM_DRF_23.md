# 타임아웃 및 재시도 처리

## 재시도
- `try-except` 블록을 활용하여 타임아웃 발생 시 작업을 일정 횟수 반복하도록 설정

```python
from time import sleep

def retry_on_timeout(func, retries=3, delay=5):
    for attempt in range(retries):
        try:
            return func()
        except TimeoutError:
            if attempt < retries - 1:
                print(f"Retrying... ({attempt + 1}/{retries})")
                sleep(delay)
            else:
                raise TimeoutError("최대 재시도 횟수를 초과했습니다.")

try:
    response = retry_on_timeout(
        lambda: llm.RAG_chain(summary, contents, memory, user_input)
    )
except TimeoutError as e:
    return Response(
        {"error": "요청 시간이 초과되었습니다. 나중에 다시 시도해주세요."},
        status=status.HTTP_408_REQUEST_TIMEOUT,
    )
```


## 사용자 알림

에러 메시지를 반환

### 코드 구현

```python
try:
    result = llm.RAG_chain(summary, contents, memory, user_input)
except TimeoutError:
    return Response(
        {
            "error": "요청 시간이 초과되었습니다.",
            "message": "서버가 응답하지 않아 처리가 중단되었습니다. 잠시 후 다시 시도해주세요.",
        },
        status=status.HTTP_408_REQUEST_TIMEOUT,
    )
```

## 비동기 처리

- `asyncio`

```python
from asgiref.sync import sync_to_async

async def post(self, request, chat_id=False):
    ...
    result = await sync_to_async(llm.RAG_chain)(summary, contents, memory, user_input)
    ...
```

## 타임아웃 값 조정

LLM 호출 함수에서 타임아웃 값 설정

```python
result = llm.RAG_chain(summary, contents, memory, user_input, timeout=30)
```

