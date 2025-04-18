# 소셜 로그인 구현

## User모델 수정
- `is_social` : 일반 사용자와 소셜로그인 사용자 구별
- `social_login` : 소셜 로그인을 통한 접근인지 구별

```py
    class User(AbstractBaseUser, PermissionsMixin):
    ...
    is_social = models.BooleanField(default=False)
    social_login = models.BooleanField(default=False)
    ...

```

## Settings.py
- `SOCIALACCOUNT_PROVIDERS` 수정
  - `APP` 또는 `APPS` 설정이 더이상 사용되지 않아 제거
- `Scope` : 제공자마다 다르기 때문에 확인 필요

```
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "github": {
        "SCOPE": [
            "read:user", "user:email"
        ],
        "AUTH_PARAMS": {
            "allow_signup": "true",  # 회원가입 허용
        },
    }
}
```

## 의존성
- 환경변수에서 **ID, Key** 가져오기

```py
import requests
from urllib.parse import urlencode
from django.shortcuts import redirect
from coding_helper.settings import (
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CALLBACK_URL,
    GOOGLE_OAUTH_CLIENT_SECRET,
    GITHUB_CLIENT_ID,
    GITHUB_REDIRECT_URI,
    GITHUB_CLIENT_SECRET,
)
```

## 소셜 로그인

### `oauth2` 인증 요청

```py
def google_login(request):
    google_oauth_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "response_type": "code",
        "client_id": GOOGLE_OAUTH_CLIENT_ID,
        "redirect_uri": GOOGLE_OAUTH_CALLBACK_URL,
        "scope": "profile email",
        "state": "state_parameter",
    }

    auth_url = f"{google_oauth_url}?{urlencode(params)}"
    return redirect(auth_url)
```

### 콜백
- 콜백 **URL**과 연결된 `GoogleLoginCallback`에 `code`가 담겨서 리다이렉션
- `code`를 추출하여 사용자 등록
  - `User` 모델을 통해 사용자 정보 입력
  - `is_social=True` , `user.social_login = True`

```py
class GoogleLoginCallback(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")

        # 인증 코드가 없으면 400 오류 반환
        if code is None:
            return Response({"error": "Authorization code not provided"}, status=400)

        # Google OAuth2 토큰 엔드포인트
        token_endpoint_url = "https://oauth2.googleapis.com/token"

        # POST 요청을 Google의 토큰 엔드포인트로 보냄
        response = (
            url=token_endpoint_url,
            data={
                "code": code,
                "client_id": GOOGLE_OAUTH_CLIENT_ID,  # 실제 client_id로 교체
                "client_secret": GOOGLE_OAUTH_CLIENT_SECRET,  # 실제 client_secret로 교체
                "redirect_uri": GOOGLE_OAUTH_CALLBACK_URL,  # 실제 redirect_uri로 교체
                "grant_type": "authorization_code",
            },
        )

        # 응답이 JSON 형식인지 확인하고 처리
        try:
            response_dict = response.json()
            access_token = response_dict["access_token"]
            url = "https://www.googleapis.com/oauth2/v3/userinfo"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_data = response.json()
            email = response_data["email"]
            id = email.split("@")[0]
            username = f"05#{id}"
            try:
                user = User.objects.get(username=username)
                print("가입된 사용자")
            except User.DoesNotExist:
                print("미가입된 사용자")

                user = User.objects.create(
                    username=username,
                    email=f"{id}@social.com",
                    first_name="Anonymous",
                    nickname=id,
                    is_active=True,
                    is_social=True,
                )
                user.save()

            user.social_login = True
            user.save()
            username = user.username

            return Response({"username": username})

        except requests.exceptions.RequestException as e:
            return Response({"error": f"Request error: {str(e)}"}, status=400)

        except ValueError:
            return Response({"error": "Invalid response from Google"}, status=400)
```