# 챗봇 앱 개선 - Redis 테스트

## `class RagChatbotView(APIView):`

### get 요청
- 캐시 존재 확인
- 없는 경우 **DB** 조회

```py
    def get(self, request, chat_id):
        try:
            user = request.user
            try:
                cache_key = f"{user.id}:{chat_id}:chathistory"
                chat_history = cache.get(cache_key)
                print("캐시호출")
            except:
                chat_history = self.get_chat_history(chat_id, user)
            return Response(
                {
                    "id": chat_history.id,
                    "title": chat_history.title,
                    "content_info": chat_history.content_info,
                    "chatlog": chat_history.conversation,
                },
                status=status.HTTP_200_OK,
            )
        except ChatHistory.DoesNotExist:
            return Response(
                {"error": "ChatHistory not found"}, status=status.HTTP_404_NOT_FOUND
            )
```

### post 요청
- `chathistory_keys` : 캐시를 호출할 때 사용할 키값들을 저장

```py
    def post(self, request, chat_id=False):
        ...
        cache_key = f"{user.id}:{chat_history.id}:chathistory"
        cache.set(cache_key, chat_history, timeout=600)

        chathistory_key = f"{user.id}:chathistory_keys"
        id = chat_history.id
        if not cache.get(chathistory_key):
            cache.set(chathistory_key, [id], timeout=600)
        else:
            keys = cache.get(chathistory_key)
            if id not in keys:
                keys.append(id)
            cache.set(chathistory_key, keys, timeout=600)

        return Response(
            {
                "id": chat_history.id,
                "AI": response,
                # "multi_query": multi_query if category == "Official-Docs" else None,
                # "Retriever": context if category == "Official-Docs" else None,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, chat_id):
        try:
            # 사용자 정보
            user = request.user
            # 특정 사용자 ID에 해당하는 ChatHistory 삭제
            ChatHistory.objects.filter(id=chat_id, user=user).delete()
            return JsonResponse({"message": f"{chat_id} 삭제"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

```

## `class ChatSessionView(APIView):`
- 대화내역 호출
- `chathistory_keys` 에 저장해둔 키값을 불러옴
    - 키에 해당하는 대화 내역을 모두 불러옴


```py
class ChatSessionView(APIView):

    def get(self, request):
        try:
            user = request.user
            try:
                chathistory_key = f"{user.id}:chathistory_keys"
                keys = cache.get(chathistory_key)
                print(keys)

                chats = []
                for key in keys:
                    cache_key = f"{user.id}:{key}:chathistory"
                    chat_history = cache.get(cache_key)
                    chats.append(
                        {
                            "id": chat_history.id,
                            "title": chat_history.title,
                            "content_info": chat_history.content_info,
                            "conversation": chat_history.conversation,
                        }
                    )
                    print("캐시호출")
                print(chats)
                return Response(
                    {"chatsession": chats},
                    status=status.HTTP_200_OK,
                )
            except:
                chats = ChatHistory.objects.filter(user=request.user).values(
                    "id", "title", "content_info", "conversation"
                )
                print("DB호출")
                return Response(
                    {"chatsession": list(chats)},
                    status=status.HTTP_200_OK,
                )
        except ChatHistory.DoesNotExist:
            return Response(
                {"error": "ChatHistory not found"}, status=status.HTTP_404_NOT_FOUND
            )
```