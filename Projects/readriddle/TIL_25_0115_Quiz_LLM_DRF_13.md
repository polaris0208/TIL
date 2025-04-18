# 프로젝트 Docker-compose 개선

## 프로젝트 구조
- 프로젝트 서비스를 세가지로 나눔
- 각각의 서비스에 `Dockerfile`을 작성하여 빌드

```
project/
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── src/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   └── ...
├── db/
├── docker-compose.yml
```

## Frontend
- `./frontend` : `Dockerfile` 이 위치한 경로
- `./frontend:/app/frontend`
  - 참조할 로컬 경로
  - 해당 설정을 통해 컨테이너 실행중에 발생하는 코드 변경사항을 실시간으로 반영
- `/app/frontend/node_modules`
  - 컨테이너의 `node_modules` 경로
- `REACT_APP_API_URL: http://localhost:8000`
  - `React` 앱이 참조할 서버 경로 : 백엔드 서버

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
```

## Backend
- `./Backend` : `Dockerfile` 이 위치한 경로
- `./Backend:/app/Backend`
  - 참조할 로컬 경로
  - 해당 설정을 통해 컨테이너 실행중에 발생하는 코드 변경사항을 실시간으로 반영

```yml
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: drf
    volumes:
      - ./backend:/app/backend 
    ports:
      - "8000:8000"
    env_file:
      - .env
    environment:
      DJANGO_SUPERUSER_USERNAME: admin
      DJANGO_SUPERUSER_EMAIL: admin@example.com
      DJANGO_SUPERUSER_PASSWORD: password
    depends_on:
      - db
    command: >
      sh -c "
      dockerize -wait tcp://db:5432 -timeout 30s &&
      python manage.py makemigrations &&
      python manage.py migrate &&
      python manage.py createsuperuser --noinput || true &&
      exec python manage.py runserver 0.0.0.0:8000
      "
 ```

 ## DB

 ```yml     
  db:
    image: postgres:15
    container_name: postgres
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"
    volumes:
      - ./db/data:/var/lib/postgresql/data # 볼륨 저장
      - ./db/init:/docker-entrypoint-initdb.d # 컨테이너 생성 시 초기화 sql 파일

  pgadmin:
    image: dpage/pgadmin4
    restart: always
    container_name: pgadmin
    ports:
      - "5050:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: pgadmin4@pgadmin.org
      PGADMIN_DEFAULT_PASSWORD: password
    # 볼륨 설정
    volumes:
      - ./db/pgadmin/:/var/lib/pgadmin

# volumes: {}
```

## 추가할 사항
- `Network`
  - 서비스간의 네트워크 연결