# Github 로그인 구현

## OAuth 설정
- 깃허브 로그인
- 설정 - 개발자 설정
- **OAuth Apps** : **URL**, **Callback URL** 설정

## `settings.py`
- `SOCIALACCOUNT_PROVIDERS`에 깃허브 설정 추가
  - 깃허브의 **OAuth** 가이드를 확인하여 `scope`, `AUTH_PARAMS` 설정

```py
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

## `views.py`
- **URL** 설정에 주의
  - 인증 : `https://github.com/login/oauth/authorize`
  - 토큰 : `https://github.com/login/oauth/access_token`
  - 사용자 정보 : `https://api.github.com/user`
- 깃허브 로그인 페이지 이동 - 로그인 - 엑세스 토큰 발급 - 사용자 정보 확인

```py
class GithubLogin(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        github_oauth_url = "https://github.com/login/oauth/authorize"
        params = {
            "client_id": GITHUB_CLIENT_ID,
            "redirect_uri": GITHUB_REDIRECT_URI,
            "scope": "read:user",
            "user:email" "state": "state_parameter",  # CSRF 방지용 state 값
        }

        # GitHub로 리디렉션
        auth_url = f"{github_oauth_url}?{urlencode(params)}"
        return redirect(auth_url)


class GitHubLoginCallback(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # GitHub에서 받은 인증 코드
        code = request.GET.get("code")

        # 인증 코드가 없으면 에러 반환
        if not code:
            return Response({"error": "Authorization code not provided"}, status=400)

        # GitHub 토큰 엔드포인트
        token_endpoint_url = "https://github.com/login/oauth/access_token"

        # POST 요청으로 액세스 토큰 요청
        response = requests.post(
            url=token_endpoint_url,
            headers={"Accept": "application/json"},
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": GITHUB_REDIRECT_URI,
            },
        )

        # 응답을 JSON 형식으로 파싱
        try:
            token_data = response.json()
            access_token = token_data.get("access_token")

            if not access_token:
                return Response({"error": "Access token not received"}, status=400)

            # GitHub 사용자 정보 가져오기
            user_info_url = "https://api.github.com/user"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(user_info_url, headers=headers)
            response_data = response.json()
            email = response_data["email"]
            address = email.split("@")
            id = address[0] + address[1][0] + address[1][1]
            username = f"07_{id}"
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