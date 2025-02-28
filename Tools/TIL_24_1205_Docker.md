# Docker
> 가상화의 표준<br>
> **Container**와 **CI/CD**로 독립성과 확장성 보장

## 개념

### CI/CD 개념

#### 용어
- **CI**
  - **Continuous Integration** : 지속적인 통합
    - 코드의 통합/자동화
- **CD**
  - **Continuos Delivery** : 지속적인 제공
    - 변경사항 테스트/자동화
  - **Continous Deployment** : 지속적인 배포
    - 배포/자동화

#### 단계

1. **코드 작성** : 코드 작성, 저장소 업로드
2. **빌드** : 소스 코드 구조화, 필요한 파일 생성
3. **테스트** : 기능의 작동 점검, 버그 수정
4. **배포** : 서버에 업로드, 사용자에게 제공

#### 배경
1. **과거**
- **폭포수 개발 방법론**
  - 오랜시간 구현 - 테스트 - 긴 주기로 배포
  - 한 단계씩 수정, 추가
  - 버그가 발견되면 다시 롤백

2. **현대**
- **Scrum, Agile**
  - 특정 주기마나 개발,테스트 및 프로덕션의 통합된 기능 출시
  - **Docker**를 통해 서버, 환경 표준화
    - 같은 환경에서 테스트, 배포 자동화
    - 지속적으로 코드 통합, 자동 배포

## 설치

### Mac OS 
- **Homebrew** 설치 필요
- `brew install docker docker-compose` : 설치
- `docker --version`, `docker-compose --version` : 버전 확인
- 공식 사이트 **Docker Desktop** 다운로드 및 설치
- `docker info` : 엔진 및 구성 확인
- 결과

```bash
Docker version 27.3.1, build ce1223035a
Docker Compose version 2.31.0
Client: Docker Engine - Community
 Version:    27.3.1
 Context:    desktop-linux
 Debug Mode: false
```
### 테스트
- `docker image pull nginx:1.25.3-alpine` : 이미지 다운로드
-  `docker image` : 이미지 확인

```bash
REPOSITORY   TAG             IMAGE ID       CREATED         SIZE
nginx        1.25.3-alpine   f2802c2a9d09   13 months ago   66.4MB
```

- `docker image history nginx:1.25.3-alpine` : `Dockerfile`에 대한 정보

```bash
IMAGE          CREATED         CREATED BY                                       SIZE      COMMENT
f2802c2a9d09   13 months ago   RUN /bin/sh -c set -x     && apkArch="$(cat …   33.3MB    buildkit.dockerfile.v0
<missing>      13 months ago   ENV NJS_VERSION=0.8.2                            0B        buildkit.dockerfile.v0
<missing>      13 months ago   CMD ["nginx" "-g" "daemon off;"]                 0B        buildkit.dockerfile.v0
<missing>      13 months ago   STOPSIGNAL SIGQUIT                               0B        buildkit.dockerfile.v0
<missing>      13 months ago   EXPOSE map[80/tcp:{}]                            0B        buildkit.dockerfile.v0
<missing>      13 months ago   ENTRYPOINT ["/docker-entrypoint.sh"]             0B        buildkit.dockerfile.v0

```

- `docker run -d -p 8001:80 --name webserver01 nginx:1.25.3-alpine` : 실행
- `docker ps | grep webserver01` : 서버 확인 

```bash
a2154fbb354f   nginx:1.25.3-alpine   "/docker-entrypoint.…"   43 seconds ago   Up 43 seconds   0.0.0.0:8001->80/tcp   webserver01
```

- `docker port webserver01` : 포트 확인
  - `80/tcp -> 0.0.0.0:8001`

- `curl localhost:8001` : 동작 확인
- `localhost:8001` : 접속 확인

```
Welcome to nginx!

If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.
Commercial support is available at nginx.com.

Thank you for using nginx.
```

## Docker Image
- 필요한 파일만 포함, 변경하려면 새로 생성
- 런타임에 필요한 바이너리, 라이브러리 및 설정갑 포함
- **Stateless** : 상태를 저장하지 않음 - 다른 환경에서도 동일한 실행
- **Immutable** : 변경할 수 없음

### 흐름
- 기본 **Resistry**는 **docker.io**
  - 기업이나 개인 또는 클라우드의 저장소를 사용하는 경우 별도 설정

```
[Dockerfile] - Build - > [Images] - Run -> [Container]
                             |
                            Push
                             |
                       [Registry/Hub]
                             | 
                            Pull
                             | 
                         [Images] - Run -> [Container]
```

### `docker pull`
- 이미지 다운로드
  - 레지스트리 지정, 라이브러리 설정 가능

```bash
docker pull library/debian:10
docker pull docker.io/library/debian:10
docker pull index/docker.io/library/debian:10
docker pull nginx:latest
# 확인
docker images
#
REPOSITORY   TAG             IMAGE ID       CREATED         SIZE
nginx        latest          fb197595ebe7   8 days ago      280MB
debian       10              58ce6f1271ae   5 months ago    176MB
nginx        1.25.3-alpine   f2802c2a9d09   13 months ago   66.4MB
```

### `docker image inspect`
- 이미지 구조 확인
- `json` 주조이기 때문에 **key**값으로 정보 조회 가능

```bash
docker image inspect --format="{{.RepoTags}} {{.Os}}" nginx:latest
# 
[nginx:latest] linux
```

### `docker images histoy` 
- `Dockerfile`에 대한 정보

### `docker login` & `docker logout`
- 터미널 환경에서 로그인 관리

### 관리
- **os**에 설치된 **Docker Desktop** 에서 실행 확인 및 관리

## Docker Container
- `Image`를 실행한 상태
- `Image`는 틀의 역할, 즉 여러개의 `Container` 생성 가능

### `docker create`
- 실행하지 않고 생성만
- `docker create -ti --name <컨테이너 이름> <이미지 이름>:<태그>`
- `docker ps -a` : 모든 컨테이너(실행 중, 중지된 상태 포함)

```bash
docker create -ti --name ubuntu2204test ubuntu:22.04
docker ps -a

CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS    PORTS     NAMES
1c49bdd2ac0c   ubuntu:22.04   "/bin/bash"   27 seconds ago   Created 
```

### `docker start`
- 시작

```bash
docker start ubuntu2204test
ubuntu2204test

CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
1c49bdd2ac0c   ubuntu:22.04   "/bin/bash"   4 minutes ago   Up 9 seconds 
```

### `docker attach`
- 실행중인 컨테이너의 입출력 연결
- 터미널에서 내부 프로세스와 직접 상호작용
- `exit` 입력으로 종료

```bash
docker attach ubuntu2204test
root@1c49bdd2ac0c:/# exit
docker ps -a

CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                        PORTS     NAMES
1c49bdd2ac0c   ubuntu:22.04   "/bin/bash"   10 minutes ago   Exited (130) 15 seconds ago
```

### `docker run`
- `create - start - attach` 가 하나의 프로세스로 실행됨

### 기타 명령어

#### 테스트 실행
- `docker run -ti -d -p 6060:6060 --name=node-test -h node-test node-test:1.0`
  - `-ti` 터미널 상호작용 가능한 상태로
    - `-t`, `-i`를 조합한 형태 : 순서는 상관없음
  - `-d` 백그라운드 모드로
  - `-p` 해당 포트에서
  - `-h` 호스트 이름
  - `node-test:1.0` 실행할 이미지 이름

```bash
mkdir nodejsapp
cd nodejsapp
vim app.js 
# 앱 작성
vim Dockerfile
# 파일 작성
docker buildx build -t node-test:1.0 . 
# node-test 라는 이름의 1.0 태그를 현재 디렉토리에서 실행
docker images | grep node-test
# node-test를 포함하는 이미지 목록만 가져오기
docker image history node-test:1.0
# 포트 정보 확인
docker run -ti -d -p 6060:6060 --name=node-test -h node-test node-test:1.0
# contrainer 실행
curl http://localhost:6060
# 실행 결과 확인
HostName: node-test
# 결과
```

#### 상태 확인
- 프로세스, 리소스, 로그 등
- `docker logs –f node-test`
  - `-f` : **follow** 옵션, 실시간 체크

```bash
docker top node-test
# container에서 실행중인 프로세스 확인
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                685                 667                 0                   06:08               ?                   00:00:00            /sbin/tini -- node app.js
root                709                 685                 0                   06:08               ?                   00:00:00            node app.js

docker port node-test
# 포트 조회
6060/tcp -> 0.0.0.0:6060
# 결과
docker stats node-test --no-stream
# container 리소스 통계 출력 -- 스트림 없이
CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
7d2849a4160d   node-test   0.02%     10.13MiB / 3.827GiB   0.26%     1.61kB / 518B   0B / 0B     8

docker logs node-test
연결 완료.
요청 처리중
```

#### `docker stop / start / pause / unpause`
- `docker stats`, `docker events` : 실행 상태 확인용

```bash
docker stop node-test
docker ps –a
# exited : 종료 처리

docker start node-test
docker pause node-test
docker ps -a
# Up 33 seconds (Paused) : 정지 처리

docker unpause node-test
docker ps -a
# Up 48 seconds : 다시 실행
```

#### `prune`
- 정리 명령어
- `docker container prune` : 실행 중 제외, 모든 컨테이너 삭제
- `docker image prune` : 태그가 붙은 것 제외, 모든 이미지 삭제
- `docker system prune` : 사용하지 않는 이미지, 컨테이너, 볼륨, 네트워크 등 모든 리소스 삭제

```bash
docker container ls -a
# 전체 컨테이너 확인
CONTAINER ID   IMAGE           COMMAND                   CREATED             STATUS                           PORTS     NAMES
7d2849a4160d   node-test:1.0   "/sbin/tini -- node …"   34 minutes ago      Exited (143) 16 seconds ago                node-test
bf75c47d16fe   ubuntu:22.04    "/bin/bash"               About an hour ago   Exited (0) About an hour ago               ubuntu2204test2
1c49bdd2ac0c   ubuntu:22.04    "/bin/bash"               About an hour ago   Exited (130) About an hour ago             ubuntu2204test

docker container prune
# 컨테이너 삭제
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N]  y  
Deleted Containers:
7d2849a4160d8a1355932233e89b8b10a26354e3a062e1e396bcf19bf2750cde
bf75c47d16feb18800304e7e617ce93bfec3b52c6b42f92fcf09d764a130dbdc
1c49bdd2ac0c627a58313bd783320edab7d931cebc27687a708a8470077f9ecf

Total reclaimed space: 28.67kB

docker image ls
# 전체 이미지 확인
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
node-test    1.0       7d655849368b   38 minutes ago   199MB
ubuntu       22.04     0e5e4a57c249   2 months ago     106MB

docker image prune
# 이미지 삭제
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N]  y
Total reclaimed space: 0B

docker system prune
# 일괄 삭제
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
Deleted build cache objects:
lb0te2y4ymrbu2u8qutsqq8lh
ieyqa9iaduyzrwo18p8lrqukx
nqvz0hswgj9phycmzpgbuu9e2

Total reclaimed space: 20.48kB
```