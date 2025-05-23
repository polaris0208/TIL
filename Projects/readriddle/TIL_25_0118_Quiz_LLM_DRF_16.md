# 챗봇 앱 개선 Redis 적용

## docker-compose에 Redis 추가

```yml
services:
  ...
  redis:
    image: redis
    container_name: redis
    ports:
      - "6379:6379"
```

## requirements.txt

```
...
django-redis
...
```

## settings.py

### `django_redis` 등록

```py
INSTALLED_APPS = [
  ...
  "django_redis",
  ...
]
```

### CACHES 설정
- `redis`를 사용하도록 설정

```py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
```

## 테스트

### `accounts` - `views.py`
- `cache_key` : `user.id`, `chat_id` 조합해서 구분
- `chat_history = cache.get(cache_key)`
  - 캐시 먼저 조회
  - 없으면 **DB** 조회
  - 없으면 새로 생성
- `cache.set(cache_key, chat_history, timeout=600)`
  - 캐시 설정
  - 대화 내용이 추가된 경우 새로운 대화내역으로 덮어쓰기
    - 덮어쓰게 동일한 키에 다른 내용인 경우

```py
class RagChatbotView(APIView):
    ...
    def post(self, request, chat_id=False):
        # 사용자 정보
        user = request.user
        # ChatHistory 조회 또는 생성
        try: 
            cache_key = f"{user.id}:{chat_id}:chathistory"
            chat_history = cache.get(cache_key)
            print('캐시 호출')
        except:
            chat_history = self.get_chat_history(chat_id, user) if chat_id else None
            content = ""

        if chat_history:
            # 기존 채팅 기반 처리
            memory = chat_history.conversation
            category = chat_history.content_info["category"]
            user_input = request.data["user_input"]

            if category == "OFFICIAL_DOCS":
                title = chat_history.content_info["title"]
                response = rag.officail_rag(title, user_input, memory)
            else:
                content = chat_history.content
                chain = llm.QnA_chain()
                response = chain.invoke(
                    {"history": memory, "question": user_input, "content": content}
                )
        else:
            # 새로운 ChatHistory 생성
            category = request.data["category"]
            title_no = request.data["title_no"]
            user_input = request.data["user_input"]

            if category == "OFFICIAL_DOCS":
                memory = [{"SYSTEM": "init conversation"}]
                documents = Documents.objects.filter(title_no=title_no).first()
                title = documents.title
                response = rag.officail_rag(title, user_input, memory)
                content_info = {
                    "category": category,
                    "title_no": title_no,
                    "title": title,
                }
            else:
                reference = Reference.objects.filter(
                    category=category, title_no=title_no
                ).first()  # 첫 번째 결과만 가져옴

                # reference가 None이 아니면 content를 사용
                if reference:
                    content = reference.content
                else:
                    content = "자료 읽기에 실패하였습니다."
                chain = llm.QnA_chain()
                response = chain.invoke(
                    {"history": [], "question": user_input, "content": content}
                )
                content_info = {"category": category, "title_no": title_no}
                memory = [{"SYSTEM": "init conversation"}]

            chat_history = ChatHistory.objects.create(
                user=user,
                conversation=memory,
                content_info=content_info,
                content=content,
            )

        # 응답 ID 생성 및 대화 기록 업데이트
        id_user, id_ai = self.generate_ids(chat_history)

        last_response_user = {"id_user": id_user, "USER": user_input}
        last_response_ai = {"id_ai": id_ai, "AI": response}

        memory.extend([last_response_user, last_response_ai])

        # ChatHistory 저장
        chat_history.title = llm.summarize_title(memory)
        chat_history.conversation = memory
        chat_history.last_response_user = last_response_user
        chat_history.last_response_ai = last_response_ai
        chat_history.save()
        cache_key = f"{user.id}:{chat_id}:chathistory"
        cache.set(cache_key, chat_history, timeout=600)
        print('캐시 저장')

        return Response(
            {
                "id": chat_history.id,
                "AI": response,
                # "multi_query": multi_query if category == "Official-Docs" else None,
                # "Retriever": context if category == "Official-Docs" else None,
            },
            status=status.HTTP_200_OK,
        )
```

