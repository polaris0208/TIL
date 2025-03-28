# JWT 토큰 커스터마이징

## `TokenObtainPairView`에서 생성된 토큰의 클레임을 커스터마이징

```python
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 커스텀 클레임 추가
        token['name'] = user.name
        token['is_admin'] = user.is_staff  # 관리자 여부 추가
        token['email'] = user.email  # 이메일 정보 추가
        
        return token
```

## `settings.py`

```python
SIMPLE_JWT = {
    # 기본 시리얼라이저(TokenObtainPairSerializer) 대신 사용될 시리얼라이저 지정
    "TOKEN_OBTAIN_SERIALIZER": "my_app.serializers.MyTokenObtainPairSerializer",
    # ...
}
```

## 로그인 뷰에서 활용

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.cache import cache
from django.contrib.auth.models import update_last_login
from my_app.serializers import UserSerializer
from my_app.models import ChatHistory, Documents, Reference

from my_app.serializers import MyTokenObtainPairSerializer

class AuthAPIView(APIView):

    def get_permissions(self):
        """POST 요청은 인증 없이 허용"""
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 로그인
    def post(self, request):
        # 유저 인증
        user = User.objects.get(username=request.data.get("username"))
        if user.social_login == False:
            user = authenticate(
                username=request.data.get("username"),
                password=request.data.get("password"),
            )
        # 이미 회원가입 된 유저일 때
        if user is not None:
            if not user.is_active:
                return Response(
                    {"message": "User is inactive"}, status=status.HTTP_400_BAD_REQUEST
                )

            login(request, user)
            update_last_login(None, user)
            serializer = UserSerializer(user)
            # jwt 토큰 접근
            token = MyTokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("username", user.username, httponly=False)
            res.set_cookie("access", access_token, httponly=False)

            user.refresh_token = refresh_token
            user.social_login = False
            user.save()
            # 사용자 캐시 초기화
            chats = ChatHistory.objects.filter(user=request.user)
            if chats:
                chathistory_key = f"{user.id}:chathistory_keys"
                keys = []
                for chat in chats:
                    cache_key = f"{user.id}:{chat.id}:chathistory"
                    cache.set(cache_key, chat, timeout=60 * 60)
                    keys.append(chat.id)
                cache.set(chathistory_key, keys, timeout=60 * 60)
                print("대화내역 캐시 등록")

            # 레퍼런스 초기화
            documents = cache.get("documents")
            if not documents:
                documents = Documents.objects.all()
                cache.set("documents", documents, timeout=60 * 60 * 24)
                print("공식문서 캐시 등록")
            reference = cache.get("reference")
            if not reference:
                reference = Reference.objects.all()
                cache.set("reference", reference, timeout=60 * 60 * 24)
                print("레퍼런스 캐시 등록")

            return res
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
```

