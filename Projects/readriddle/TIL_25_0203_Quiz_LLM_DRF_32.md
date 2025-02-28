# 프로젝트 피드백 반영

## Django 서버 변경
- 개발용 `runserver` 에서 변경
  - `daphne` 서버로 변경

```py
# backend/coding_helper/asgi.py
import django
from django.core.asgi import get_asgi_application

# Django 환경 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coding_helper.settings")
django.setup()  # Django 앱을 명시적으로 로드

from chat.routing import websocket_urlpatterns  # django.setup() 이후에 import

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
```

```py
# docker-compose.yml
      ...
      dockerize -wait tcp://db:5432 -timeout 30s &&
      python manage.py makemigrations &&
      python manage.py migrate &&
      exec daphne -b 0.0.0.0 -p 8000 coding_helper.asgi:application
      "
      ...
```

## 와일드 카드 및 `all` 필드 제거
- 순환 참조 방지 및 사용한 라이브러리 파악에 용이하게 수정

```py
        # 변경 전
        fields = "__all__"

        # 변경 후
        fields = [
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "nickname",
            "birth_date",
            "gender",
            "intro",
            "RiddleScore",
            "is_superuser",
            "is_active",
            "is_social",
            "social_login",
            "is_staff",
            "created_at",
            "updated_at",
            "refresh_token",
        ]
```

```py
# 변경 전
from .views import *

# 변경 후
from .views import (
  SignInOutAPIView,
  ProfileAPIView,
  TokenRefresh,
  AuthAPIView,
  PasswordAPIView,
  GoogleLogin,
  GoogleLoginCallback,
  GithubLogin,
  GitHubLoginCallback
)
```

## Dokcer 설정 수정

### Dockerfile 수정
- 중복된 `apt-get update && \` 명령어 통일
- `docker-compose` 파일과 중복되는 포트 설정 제거

```yml
FROM python:3.10-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends postgresql-client wget && \
    rm -rf /var/lib/apt/lists/* && \
    wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && \
    tar -xvzf dockerize-linux-amd64-v0.6.1.tar.gz && \
    mv dockerize /usr/local/bin/
    
# 작업 디렉토리 설정
WORKDIR /app/backend

# 종속성 설치를 위한 requirements.txt 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .
```

### docker-compose.yml 수정
- `redis:7.4.2` : 이미지에 버전 명시
  - `lastest` 의 경우 새로운 버전이 적용되면 문제 발생 우려
- `${POSTGRES_VOLUME}` : 민감 정보 환경 변수화
  - `postgres` 계정 정보, `DB` 경로

```yml
services:
  frontend:
    build:
      context: ./frontend
    volumes:
      - ./frontend:/app/frontend
      - /app/frontend/node_modules
    ports:
      - "3000:3000"
    env_file:
      - .env
    environment:
      REACT_APP_API_URL: http://localhost:8000

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: drf
    volumes:
      - ./backend:/app/backend 
    env_file:
      - .env
    environment:
      REDIS_HOST: redis
    depends_on:
      - db
      - redis
    command: >
      sh -c "
      dockerize -wait tcp://db:5432 -timeout 30s &&
      python manage.py makemigrations &&
      python manage.py migrate &&
      exec daphne -b 0.0.0.0 -p 8000 coding_helper.asgi:application"
      
  db:
    image: postgres:15
    container_name: postgres
    restart: always
    env_file:
      - .env
    ports:
      - "5432:5432"
    volumes:
      - ${POSTGRES_VOLUME} # 볼륨 저장
      - ${POSTGRES_INIT} # 컨테이너 생성 시 초기화 sql 파일

  pgadmin:
    image: dpage/pgadmin4
    restart: always
    container_name: pgadmin
    env_file:
      - .env
    ports:
      - "5050:80"
    # 볼륨 설정
    volumes:
      - ${PGADMIN_VOLUME}

  redis:
    image: redis:7.4.2
    container_name: redis
    ports:
      - "6379:6379"


  nginx:
    image: nginx:1.27.3
    container_name: nginx
    restart: always
    env_file:
      - .env
    ports:
      - "80:80"
    depends_on:
      - backend
      - frontend
    volumes:
      - ${NGINX_VOLUME}
      - ${NGINX_STATIC}
      - ${NGINX_MEDIA}
```