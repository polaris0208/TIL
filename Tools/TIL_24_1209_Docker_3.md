# Docker Volume

## 개념
- 컨테이너가 종료되거나 삭제되면 데이터도 삭제
- Docker Volume을 사용하여 데이터를 안전하게 보관

## 필요성
- 데이터 영속성
- 데이터 공유: 여러 컨테이너가 동일한 볼륨을 공유하여 데이터를 사용하거나 수정
- 데이터 백업 및 이동: 볼륨을 사용하면 데이터를 백업하거나 다른 시스템으로 이동하는 것이 용이

## Volume 생성 및 활용

### Volume 생성

- `docker volume create datavol`
  - `docker volume create` : 볼륨을 새로 생성하는 명령어
  - `datavol`: 생성할 볼륨의 이름

- `docker volume ls`
  - 모든 볼륨을 나열하는 명령어

### Volume 사용 예시

- `docker container run -ti --rm -v datavol:/data alpine`
  - `docker container run` : 새로운 컨테이너를 실행
  - `-ti`
    - `-t` : **TTY(터미널 인터페이스)**를 활성화하여 컨테이너에서 인터랙티브하게 작업
    - `-i` : 표준 입력을 유지
  - `--rm` : 컨테이너가 종료되면 자동으로 삭제
  - `-v datavol:/data` : `datavol`이라는 볼륨을 `/data` 디렉토리로 마운트, 컨테이너 종료 후에도 유지
  - `alpine`: 컨테이너가 실행될 이미지를 지정
    - `alpine` : 가볍고 빠른 리눅스 기반의 이미지

#### 결과
> 컨테이너가 실행되면, 해당 컨테이너에서 /data 디렉토리에 데이터가 저장되고 컨테이너가 삭제된 후에도 볼륨에 존재

### Volume에 데이터 쓰기
- 볼륨에 데이터를 추가하거나 수정
- `echo "볼륨 데모" > /data/demo.txt`
  - `/data/demo.txt` 파일에 `"볼륨 데모"`라는 내용을 작성

### 컨테이너 종료 후 데이터 확인
- `docker container ls` : 종료 확인
- `docker container run --rm -v datavol:/data ubuntu cat /data/demo.txt`
  - `ubuntu`: **ubuntu** 이미지를 사용하여 컨테이너를 실행
  - `cat /data/demo.txt`: 파일의 내용을 출력

#### 결과
> 이전에 작성한 "볼륨 데모"라는 내용이 출력

### Volume의 위치 확인
- 시스템의 볼륨 저장 경로를 탐색
- `sudo apt update; sudo apt install -y tree`
  - `sudo apt update`: 로컬 패키지 목록을 업데이트하여, 최신 패키지 정보를 가져옴
  - `sudo apt install -y tree`: tree 패키지를 설치
    - `tree` : 디렉토리 구조를 트리 형태로 보여주는 유틸리티
    - `-y` 플래그는 설치 중에 나오는 모든 확인 요청에 대해 자동으로 "예"를 답변
  - `;` : 여러 코드 한줄에 실행, 앞의 코드가 실패해도 뒤의 코드 실행
    - `&&` : 모두 설공해야 실행
- `sudo tree -a /var/lib/docker/volumes/datavol`
  - `tree -a /var/lib/docker/volumes/datavol`
    - 볼륨이 저장되는 경로 확인
    - 트리 형태로 확인

### Docker Volume Inspect
- 볼륨의 세부 정보를 확인
  - 이 정보를 통해 볼륨의 생성 시간, 드라이버, 저장 경로 등을 확인
- `docker volume inspect datavol`

## Bind Mount
- 호스트 시스템의 특정 디렉토리나 파일을 컨테이너에 마운트하여 사용
- **Docker Volume**과 달리 **Docker**가 파일을 관리하지 않고, 호스트 시스템의 파일을 그대로 사용

### 특징
- 호스트 파일 시스템 직접 사용
- 상호작용 가능
  - 호스트에서 파일을 수정하면 컨테이너 내부에서 실시간으로 반영
  - 컨테이너 내부에서 파일을 수정하면 호스트에서도 바로 반영
- 유연성

### 사용 예시

### 마운트

- `cd ~`: 홈 디렉토리로 이동
- `mkdir test-app`: `test-app` 디렉토리를 생성
- `cd test-app`: t`est-app` 디렉토리로 이동
- `touch run.sh`: `run.sh`라는 빈 쉘 스크립트 파일을 생성
- `chmod +x ./run.sh`: `run.sh` 파일에 실행 권한을 부여
- `docker run -ti --rm -v .:/app alpine`
  - `-v .:/app`: 호스트 시스템의 `test-app` 디렉토리를 컨테이너 내부의 `/app` 디렉토리에 마운트
    - 호스트의 `test-app` 디렉토리와 컨테이너 `/app` 디렉토리 상호작용
  - `alpine`: 가벼운 리눅스 기반 이미지를 사용

```bash
cd ~
mkdir test-app
cd test-app
touch run.sh
chmod +x ./run.sh
docker run -ti --rm -v .:/app alpine
```

### 결과 확인
- 컨테이너 내부에서 `/ap` 디렉토리로 이동하여 `run.sh` 파일을 확인 가능
- `cd /app`: 컨테이너 내부의 `/app` 디렉토리로 이동
- `ls -ahlvF`: 해당 디렉토리의 내용을 확인

```bash
cd /app
ls -ahlvF
```

### Read-Only와 Read-Write Bind Mount
- 마운트한 디렉토리나 파일을 **읽기 전용(read-only)** 또는 **읽기-쓰기(read-write)** 로 설정


#### 읽기 전용 마운트
- `-v ~/readonly:/readonly:ro` 
  - 호스트 시스템의 `readonly` 디렉토리를 컨테이너의 `/readonly` 디렉토리로 마운트
  - `ro` : **read-only** 읽기 전용으로 설정 
- `-v ~/readwrite:/readwrite:rw` 
  - 호스트 시스템의 `readwrite` 디렉토리를 컨테이너의 `/readwrite` 디렉토리로 마운트
  - `rw` : **read-write** 읽기-쓰기 가능으로 설정 

```bash
cd ~
mkdir readonly
mkdir readwrite
docker run -ti -v ~/readonly:/readonly:ro -v ~/readwrite:/readwrite:rw ubuntu
```

#### 결과 확인

```bash
echo "test" > /readonly/readonly.txt # 파일을 쓸 수 없음
echo "test" > /readwrite/readwrite.txt # 파일 쓰기 가능
```


### Tmpfs Mount
- 메모리 기반의 파일 시스템을 사용하여 데이터를 임시로 저장하는 방식
- 컨테이너가 종료되면 데이터도 삭제
- 주로 빠른 데이터 접근이 필요하거나, 일시적인 데이터를 저장할 때 사용
- `docker run -ti --rm --tmpfs /tmp:rw,size=100m alpine`
  - `--tmpfs /tmp:rw,size=100m`
    - 컨테이너 내부의 `/tmp` 디렉토리를 마운트
    - 크기를 100MB로 설정
  - `rw`: 읽기-쓰기 가능하게 설정

## MySQL 데이터를 보존하기
- `Bind Mount`와 `Volum`e을 사용하여 MySQL 데이터를 보존
- `docker run -ti --rm -d --name mysqltest -e MYSQL_ROOT_PASSWORD=123! -e MYSQL_DATABASE=mysqltest -v ~/mysqldata:/var/lib/mysql mysql:latest`
  - `-e MYSQL_ROOT_PASSWORD=123!`: MySQL의 루트 비밀번호를 설정합니다.
  - `-e MYSQL_DATABASE=mysqltest`: mysqltest라는 데이터베이스를 생성
  - `-v ~/mysqldata:/var/lib/mysql`: 호스트 시스템의 mysqldata 디렉토리를 MySQL 컨테이너의 데이터 저장 경로인 /var/lib/mysql로 마운트
  - `mysql:latest`: **MySQL**의 최신 이미지를 사용하여 컨테이너를 실행

### 작성

```bash
docker exec -ti mysqltest /bin/bash
# mysqltest 컨테이너에 접속하여 쉘을 실행
mysql -h localhost -u root -p
# MySQL에 접속

show databases;
use mysqltest;
create table mysqltest(id int, name varchar(50));
insert into mysqltest values(1, 'testname');
select * from mysqltest;
```

### 데이터 지속성 확인
- 컨테이너를 중지하고 동일한 데이터를 가진 다른 컨테이너를 실행하여, 데이터가 보존되었는지 확인

```bash
docker stop mysqltest
# 기존의 mysqltest 컨테이너를 중지
docker run -ti --rm -d --name mysqltest2 -e MYSQL_ROOT_PASSWORD=123! -e MYSQL_DATABASE=mysqltest -v ~/mysqldata:/var/lib/mysql mysql:latest
# 동일한 데이터가 담긴 새로운 mysqltest2 컨테이너를 실행

docker exec -ti mysqltest2 /bin/sh
mysql -h localhost -u root -p
use mysqltest;
select * from mysqltest;
# 이전에 삽입한 데이터를 확인
```

# Docker Network
- 컨테이너들이 서로 통신할 수 있도록 지원하는 네트워크 시스템
- 컨테이너들 간의 원활한 데이터 전송과 보안적인 격리가 실현

## Docker Container Network Model (CNM)
- 컨테이너가 통신할 수 있는 네트워크 모델
- 여러 개의 컨테이너들이 어떻게 서로 소통하고, 외부 네트워크와 상호작용할 수 있는지를 정의
- **Sandbox**
  - 컨테이너를 외부 세계로부터 분리하여 안전한 환경을 제공
  - 외부에서 들어오는 네트워크 연결은 차단됩니다.
- **Endpoint**
  - 샌드박스와 외부 세계를 연결하는 지점으로
- **Network**: 컨테이너들 간의 데이터 전송을 위한 경로

## Docker Network 종류
- **Bridge Network**
  - 기본 네트워크 유형
  - 한 호스트 내에서 여러 컨테이너가 서로 통신
  - 포트 매핑을 사용하면 외부 네트워크와도 연결이 가능
- **Public Network**
  - 외부에서 접근할 수 있도록 포트를 열거나, 호스트 네트워크를 사용하여 컨테이너가 호스트의 네트워크를 직접 사용
- **Private Network**
  - 특정 컨테이너들만 연결되는 네트워크입니다. 외부와는 격리되어, 보안성을 강화
  - 사용자가 직접 네트워크를 만들고 컨테이너를 그 네트워크에 연결하여 통신

### 예시: 웹 API, 제품 카탈로그, 데이터베이스 서비스 설정

#### 네트워크 생성
- `--driver=bridge`: `bridge` 드라이버를 사용하여 네트워크를 생성
  - 기본적으로 제공하는 네트워크 유형으로, 컨테이너가 호스트 내에서 통신

```bash
docker network create --driver=bridge back
docker network create --driver=bridge front
```

#### 컨테이너 생성 및 실행
- 해당 서비스를 어떤 네트워크에 연결할지 지정
- `--name`: 컨테이너의 이름을 지정
- `-itd`: 
  - `-i` **interactive**와 `-t` **ㅆTTY**를 결합하여 터미널을 연결
  - `-d` **detached** 옵션으로 백그라운드에서 실행
- `--net`: 컨테이너가 연결될 네트워크를 지정

```bash
docker run --name=webapi -itd --net=front ubuntu:14.04
docker run --name=catalog -itd --net=back ubuntu:14.04
docker run --name=database -itd --net=back ubuntu:14.04
```
#### catalog 서비스 front 네트워크 연결
- `docker network connect front catalog`
- `catalog` 컨테이너를 `front` 네트워크에 추가
- `catalog`는 `front` 네트워크에 속한 컨테이너들과도 통신 가능

#### 각 서비스의 라우팅 테이블 확인
- `docker exec <컨테이너 이름> route`: 해당 컨테이너 내부의 라우팅 테이블을 확인하여 네트워크 연결 상태 확인

```bash
docker exec webapi route
docker exec catalog route
docker exec database route
```

#### 네트워크 상태 확인
- 네트워크에 연결된 컨테이너 목록을 확인

```bash
docker network inspect front  # webapi, catalog 연결 확인
docker network inspect back   # catalog, database 연결 확인
```

#### 네트워크 테스트
- `webapi`는 `front` 네트워크에 연결되어 있지만 `back` 네트워크에는 연결되지 않았기 때문에 database와는 통신 불가
- `catalog`는 두 네트워크에 연결되어 있으므로 `webapi`와 `database` 모두와 통신 가능

```bash
# webapi 컨테이너에 접속하여 테스트
docker exec -it webapi bash

# webapi에서 catalog는 핑 가능
ping -c 1 catalog  # 가능

# webapi에서 database는 핑 불가능
ping -c 1 database  # 불가능

exit

# catalog 컨테이너에 접속하여 테스트
docker exec -it catalog bash

# catalog에서 webapi와 database는 모두 핑 가능
ping -c 1 webapi  # 가능
ping -c 1 database  # 가능

exit
```

#### 네트워크 분리 및 리소스 정리
모든 테스트를 완료한 후, catalog를 front 네트워크에서 분리하고, 컨테이너와 네트워크를 삭제하여 리소스를 정리

```bash
# catalog를 front 네트워크에서 분리
docker network disconnect front catalog

# 컨테이너 종료 및 삭제
docker stop webapi catalog database
docker rm webapi catalog database

# 네트워크 삭제
docker network rm back
docker network rm front
```