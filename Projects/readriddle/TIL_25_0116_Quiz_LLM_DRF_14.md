# 소셜 로그인 - Google

## [구글클라우드](https://console.cloud.google.com/) 접속
- 회원가입
- 프로젝트 생성
- 빠른 엑세스 - **API** 및 서비스 접속

### API 및 서비스
- 사용자 인증 정보
    - 사용자 인증 정보 만들기
    - **OAuth 2.0** 클라이언트 **ID**
    - 애플리케이션 유형
        - 웹 애플리케이션
        - 이름
        - 리다이렉션 **URL** 등록
- **OAuth 2.0** 클라이언트 **ID** 확인 사항
    - 클라이언트 **ID**
    - 클라이언트 보안 비밀번호
    - 리다이렉션 **URL**
        - 사이트 **URL**
        - 콜백 **URL** : 소셜 로그인 후 응답 받을 **URL**

- **OAuth** 동의 화면
    - 개시상태 : 프로덕션 단계 (허용)

## 의존성 설치
- `pip install 'dj-rest-auth[with_social]'`
    - `[]`로 인해 오류 발생
    - `' '`로 감싸서 입력
- `requirements.txt`로 설치시에는 문제 없음

```py
djangorestframework-simplejwt==5.3.1  # JWT 토큰 구현
dj-rest-auth[with_social]==6.0.0       # 소셜 인증을 위한 패키지
```

## `settings.py`

### 환경변수 설정

```py
import os
from dotenv import load_dotenv

GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_OAUTH_CALLBACK_URL = os.getenv("GOOGLE_OAUTH_CALLBACK_URL")
```

### 앱 등록
- `django.contrib.sites` : 관리자 계정에서 사이트 수정을 위한 섹션 추가
- `Third party` : 소셜 로그인을 위한 패키지

```py
INSTALLED_APPS = [
    ...
    # site 섹션 추가
    'django.contrib.sites',
    # Third party
    "rest_framework_simplejwt",
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'dj_rest_auth.registration',
    ...
]
```

### MIDDLEWARE 등록
- `allauth` : 소셜 인증용 미들웨어 등록

```py
MIDDLEWARE = [
    ...
    # Third party
    ...
    "allauth.account.middleware.AccountMiddleware",
    ...
]
```

### ACCOUNT 설정
- 소셜 로그인 : 이미 다른 방법으로 사용자의 신원을 확인한 경우 이메일 인증을 생략하고 싶을 때 사용

```py
ACCOUNT_AUTHENTICATION_METHOD = "email"  # 이메일 인증 방식
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"  # 이메일 확인을 요구하지 않음
```

### SITE_ID 등록
- 1번으로 등록
- 추후에 관리자 페이지에서 1번으로 식별되지 않을경우 수정

```py
SITE_ID = 1
```

### SOCIALACCOUNT_PROVIDERS
- 여기서 설정하는 경우 관리자 페이지의 소셜 어플리케이션 설정 생략
- `SCOPE` : 소셜 로그인 후 **Google**로 부터 제공받을 정보
- `google` : 소셜로그인 제공자

```py
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APPS": [
            {
                "client_id": GOOGLE_OAUTH_CLIENT_ID,
                "secret": GOOGLE_OAUTH_CLIENT_SECRET,
                "key": "",
            },
        ],
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
```

## `admin.py` 수정
- `accounts` 앱의 `admin.py` 수정
- `admin` 페이지의 `site` 설정에 **ID** 를 확인 할 수 있도록 재정의

```py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from .models import User

# 기존 User 모델 등록
admin.site.register(User, UserAdmin)

# Site 모델 커스터마이징
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'name')  # id 표시
    ordering = ('id',)  # id 기준 정렬

# 기존 Site 모델을 다시 등록
admin.site.unregister(Site)  # 기본 Site 등록 해제
admin.site.register(Site, SiteAdmin) # 재정의 한 Site 등록
```

## `views.py`

### 의존성 설치

```py
import requests
from urllib.parse import urlencode
from django.shortcuts import redirect
from coding_helper.settings import (
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CALLBACK_URL,
    GOOGLE_OAUTH_CLIENT_SECRET,
)
```

### 구글 로그인
- 요청이 들어오면 파라미터를 포함하여 구글 로그인 페이지로 리다이레트
- 파라미터
    - `"response_type": "code"` : 코드 요청 / `access_token`
    - `client_id` : **OAuth 2.0** 클라이언트 **ID**
    - `redirect_uri` : 로그인에서 구글에서 결과를 보낼 **URL**
    - `scope` : 응답에 포함될 내용
    - `state` : 파라미터

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
- `code = request.GET.get("code")`
    - 구글 로그인 후 `"redirect_uri"`으로 `code`가 반환됨
- `requests.post(url=token_endpoint_url, data={"code": code,...)`
    - `token_endpoint_url` 로 `code`를 보냄
- `response` : `access_token` 정보가 포함된 응답
- `response = requests.get(url, headers=headers)`
    - `headers` 에 `access_token` 을 포함하여 요청을 보냄
    - 응답에는 로그인한 구글 사용자의 정보가 포함되어 반환
    - 반환된 사용자 정보 : `scope` 에서 지정한 `"profile email"`
        - 메일 주소, 프로필 이름, 프로필 사진

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
        response = requests.post(
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

        except ValueError:
            return Response({"error": "Invalid JSON response from Google"}, status=400)

        # 응답을 그대로 반환 (토큰 정보 등)
        return Response(response_data, status=200)
```

## `urls.py`
- `google/callback/`
    - **OAuth 2.0** 설정에서 설정했던 콜백 **URL**

```py
# Google 로그인 관련 URL
urlpatterns += [
    path("google/", google_login, name="google_login"),
    path("google/callback/", GoogleLoginCallback.as_view(), name="google_login_callback"),
]
```

## 테스트
- `'google-login-page/'` 에 접속하여 버튼 클릭
- 구글 로그인 페이지로 이동
- 로그인 완료할 경우 토큰과 계정 정보를 응답으로 받음

### 템플릿
- `settings.py` 경로 설정
- 루트 디렉토리에 `templates` 생성
- `google_login.html` 작성
    - `csrf_token` 포함한 `POST` 요청을 `google_login` **URL** 로 보내는 버튼 생성

```
TEMPLATES = [
    {
        ...
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        ...
            ],
        },
    },
]
```

### `urls.py`
- `accounts` 앱

```py
urlpatterns += [  # 구글 로그인 처리
    path('google-login-page/', google_login_page, name='google_login_page'),  # 구글 로그인 버튼이 있는 페이지
]
```

### `views.py`
- `accounts` 앱

```py
def google_login_page(request):
    return render(request, "google_login.html")
```