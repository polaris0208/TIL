  # Django EC2 배포

  ## Mac 사전 설정
  - 네트워크 설정
    - 22포트를 허용하는 네트워크로 변경
    - VPN, 방화벽 설정 끄기
    - 공유/인터넷 공유 설정
      - SSH 접속 설정 담당

  ## EC2 인스턴스 생성
  - **AWS Management Console**에서 EC2 인스턴스를 생성
    - Ubuntu 24.04 LTS AMI 선택
    - 인스턴스 유형은 `t2.micro` 선택 (프리티어)
    - 보안 그룹 설정 시, HTTP(80), TCP(8000), SSH(22) 포트 열기

  ## Django 배포 설정
  - `settings.py`
    - `DEBUG = False`
    - `ALLOWED_HOSTS = ['<ec2-public-ip>']`

  ## 터미널을 통해 SSH 접속
  로컬 터미널에서 EC2 인스턴스에 SSH로 접속
  ```bash
  ssh -i <발급 받은 키 파일> ubuntu@<your-ec2-public-ip>
  ```

  ## 필수 패키지 설치
  ### APT 업데이트:
  ```bash
  sudo apt update
  sudo apt upgrade -y
  ```

  ### Git 설치:
  ```bash
  sudo apt install git -y
  ```

  ### Docker 설치:
  ```bash
  sudo apt install docker.io -y
  ```

  ### Docker Compose 설치:
  ```bash
  sudo apt install docker-compose -y
  ```

  ## 4. 프로젝트 클론
  Django 프로젝트를 EC2 인스턴스로 복제
  ```bash
  git clone https://github.com/<username>/<project>.git
  cd <yourproject>
  ```

  ## 5. `.env` 파일 작성 (Django Secret 설정)
  - `.env` 파일을 생성하여 Django 비밀 키, 데이터베이스 연결 정보 등을 설정
  ```bash
  sudo vim .env
  ```
  - `.env` 예시:
  ```
  DJANGO_SECRET_KEY=<secret-key>
  ```

  ## 6. Docker Compose를 이용해 서비스 시작
  `docker-compose.yml` 파일을 확인하고, 설정이 맞는지 확인한 후 아래 명령어로 서비스를 빌드하고 실행
  ```bash
  sudo docker-compose up --build -d
  ```