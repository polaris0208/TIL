# Docker 2
> 직접 작성한 파이썬 코드로 **github actions** 테스트

## Github Actions
- **Github**에 내장된 **CI/CD** 도구
    - **github**와 통합이 용이
    - **CI/CD** 서버 내장
    -  일정 수준까지 가격이 무료
        - 무료 버전 : 스토리지 500MB, 월 2000분
- **Github Actions** 동작 방법
    - **repository**의 `.github/workflows` 디렉토리 생성
    - 필요한 **Actions** 파일들을 `yaml` 형식으로 작성

### CI
- 변경사항이 **Push, Merge. Pullrequest** 되는 경우
  - 자동으로 테스트 실행

#### 예시 프로젝트 생성

```
project/
├── calc/
│   └── calculator.py
├── test_calculator.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── python-tests.yml
```

#### `calculator.py`
- 간단한 계산 기능

```py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

#### `test_calculator.py`
- `pytesy` : **Python** 테스트 프레임워크
  - `test_*.py` 또는 `*_test.py` 처럼 `test`가 포함된 파일을 찾아 테스트
  - `assert` 뒤에 오는 표현식이 `True`인지 확인
  - `@pytest.mark.parametrize` : 여러개의 파라미터를 테스트

```py
import pytest
from src.calculator import add, subtract, multiply, divide

# 기본 테스트
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

# 예외 처리 테스트
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    with pytest.raises(ValueError):
        divide(10, 0)

# 파라미터화 테스트
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected
```

#### `requirements.txt`
- 테스트에 필요한 의존성 파일 등록
- `pytest` 추가

#### `python-tests.yml`
- 실행 : `main`, `develop` 에서 **push** 또는 **PR** 한 경우
- 작업 : `build` - `ubuntu-latest` 환경에서 진행
- 단계
  - `repository` 확인
  - **Python** 준비
  - 의존성 파일 설치 : `pip`, `pytest`
  - `pytest -v`
    - `pytest`: 테스트 실행
    - `-v` : 상세하게(**verbose**) 출력 / 테스트 케이스의 이름, 실행 순서, 통과/실패 정보를 더 명확하게 표시

```yaml
name: Run Python Tests

on: 
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps: 
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -v
```

#### 테스트 결과
- `main` 에서 **push**

```bash
Current runner version: '2.321.0'
Operating System
Runner Image
Runner Image Provisioner
GITHUB_TOKEN Permissions
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@v4' (SHA:11bd71901bbe5b1630ceea73d27597364c9af683)
Download action repository 'actions/setup-python@v4' (SHA:65d7f2d534ac1bc67fcd62888c5f4f3d2cb2b236)
Complete job name: build
...
Run pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.20, pytest-8.3.4, pluggy-1.5.0 -- /opt/hostedtoolcache/Python/3.9.20/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/CI-CD_sample/CI-CD_sample
collecting ... collected 8 items

test_calculator.py::test_add PASSED                                      [ 12%]
test_calculator.py::test_subtract PASSED                                 [ 25%]
test_calculator.py::test_multiply PASSED                                 [ 37%]
test_calculator.py::test_divide PASSED                                   [ 50%]
test_calculator.py::test_add_parametrize[1-1-2] PASSED                   [ 62%]
test_calculator.py::test_add_parametrize[2-3-5] PASSED                   [ 75%]
test_calculator.py::test_add_parametrize[-1--1--2] PASSED                [ 87%]
test_calculator.py::test_add_parametrize[0-5-5] PASSED                   [100%]

============================== 8 passed in 0.03s ===============================
```

### CD
- 테스트 완료 후 자동으로 배포
- 배포를 위한 **TOKEN** 설정
- `Repository/Settings/Security/Secrets and variables/Actions`
  - `github token` : `Profile/Settings/Developer settings/Persinal access tokens/Tokens (classic)`
    - 권한 설정 : `repo, workflow, admin:punlic_key`
  - **Cloudtype API Key** : **Github** 계정으로 가압후 발급
    - 결제 방법 등록 후 무료 사용 가능

#### 예시 프로젝트 배포
- 워크스페이스 생성 : `polaris0208`
- 프로젝트 생성 : 레포지토리와 연결 / `ci-cd-sample`
- **YAML** 파일 작성 : `deploy_main.yml`

```yaml
name: Deploy to Cloudtype

on:
  push:
    branches:
      - main  # main 브랜치에 푸시가 발생하면 배포가 진행됨
  workflow_dispatch:  # 수동으로 배포 실행 가능

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # 1. 코드 체크아웃
      - name: Checkout
        uses: actions/checkout@v3

      # 2. 배포 키 연결
      - name: Connect deploy key
        uses: cloudtype-github-actions/connect@v1
        with:
          token: ${{ secrets.CLOUDTYPE_TOKEN }}  # Cloudtype 배포 토큰
          ghtoken: ${{ secrets.GHP_TOKEN }}  # GitHub 토큰

      # 3. 배포 실행
      - name: Deploy
        uses: cloudtype-github-actions/deploy@v1
        with:
          token: ${{ secrets.CLOUDTYPE_TOKEN }}  # Cloudtype 배포 토큰
          project: polaris0208/ci-cd-sample  # 워크스페이스 이름/프로젝트 이름
          stage: main  # 배포할 스테이지 (예: main)
          yaml: |
            name: ci-cd-sample  # 프로젝트 이름
            app: python@3.9  # 앱 이름 및 버전 (예: python@3.9)
            options:
              ports: 8080  # 앱에서 사용할 포트
            context:
              git:
                url: git@github.com:${{ github.repository }}.git  # GitHub 레포지토리 URL
                ref: ${{ github.ref }}  # Git 참조 (브랜치 또는 태그)
              preset: python-flask  # 앱 종류 (예: Flask)
```

#### 결과
- `start` 설정을 하지 않아서 실행은 되지 않음
  - `flask` 또는 `fastapi` 등으로 실행 설정 필요

```
Run cloudtype-github-actions/connect@v1
⭐ Connect polaris0208/CI-CD_sample with (your) scope ghtoken is ***
👀 Deploy Key is .... polaris0208@cloudtype
✅ Success - init

Run cloudtype-github-actions/deploy@v1
🚀 1 description(s) will be deployed.
👌 Target project is @polaris0208/ci-cd-sample
 └ stage: main
🎉 1 apps deployed
✅ Success - deploy
```

## Dockerfile
- **Docker Image**를 만들기위한 환경 설정

### 작성

```yaml
# 베이스 이미지 선택
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 환경 변수 설정
ENV GREETING="Hello from Docker!"

# 애플리케이션 코드 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "app.py"]
```

### app 작성

```py
import os

def main():
    # 환경 변수 GREETING 가져오기, 기본값 설정
    greeting = os.getenv("GREETING", "Hello, World!")
    print(greeting)

if __name__ == "__main__":
    main()
```

### `requirements.txt` 작성

```
flask
```

### 빌드 및 실행

```bash
docker build -t python-app .
# 이름 디렉토리
docker run python-app
# 실행
Hello from Docker!
# 결과
```

## Docker Compose
- 여러 컨테이너의 설정을 `YAML` 파일 형식으로 정의
- 네트워크 설정, 환경 변수, 볼륨 관리 등을 간단하게 설정

### `docker-compose.yml`
- `web` - `db` 로 구성
  - `db` 가 구동 되면 `web` 구동
  - `db` : `PostgreSQL` 
    - 오픈소스 관계형 데이터베이스 관리 시스템
    - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` 환경 변수를 통해 사용자, 비밀번호, 데이터베이스를 설정
  - `DATABASE_URL=postgres://postgres:password@db:5432/mydatabase`
    - `PostgreSQL` 데이터베이스에 연결하기 위한 **URL** 형식
    - `postgres://:` : `PostgreSQL` 데이터베이스를 가리키며, 기본적으로 `postgresql` 또는` postgres`를 사용
    - `postgres:` : 사용자의 이름
    - `password@` : 사용자의 비밀번호입니다. 실제 사용 시에는 보안상의 이유로 이 비밀번호를 더 안전한 방식으로 저장하거나 환경 변수로 설정
    - `db:` : 서버가 실행되는 호스트 이름
    - `5432` : 기본 포트
    - `mydatabase` : 데이터베이스의 이름

```yaml
services:
  web:
    build: .
    container_name: python-web
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgres://postgres:password@db:5432/mydatabase
    volumes:
      - .:/app
    depends_on:
      - db

  db:
    image: postgres:13
    container_name: python-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydatabase
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### `requirements.txt` 추가

```
Flask==2.3.2
psycopg2-binary==2.9.6
Werkzeug==2.3.4
```

### `app.py`
- `db`에 접속하여 `user`를 검색 후 문자열에 포함
- `conn.cursor()` : `db`에 **SQL** 쿼리 입력
- `fetchall()` : 검색된 항목 모두 가져오기

```py
import os
from flask import Flask
import psycopg2

app = Flask(__name__)

# PostgreSQL 데이터베이스 연결
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres:password@db:5432/mydatabase')

@app.route('/')
def hello_world():
    # 데이터베이스 연결
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # users 테이블에서 데이터 조회
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    
    # 연결 종료
    cursor.close()
    conn.close()
    
    # 결과를 문자열로 반환
    return f"Hello, World! Users: {users}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

### 실행
- `docker-compose up --build`

## 모니터링
- `docker stats` : 시스템 자원 사용량 확인
- `htop` : 실시간 모니터링, 프로세스 관리