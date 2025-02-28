# API & Gemerative Model use
> **API** 및 모델의 사용방법 기초<br>
>[¶ API 활용](#api-활용)<br>
>[¶ 생성형 모델 활용](#생성형-모델-활용)

# API 활용

## Model Serving 
> 학습된 머신러닝 모델을 실제 애플리케이션에서 사용할 수 있도록 **API**를 통해 제공

### RESTful API
- **REST(Representational State Transfer)**
  - 아키텍처 스타일을 따르는 API로, HTTP를 통해 클라이언트와 서버 간에 데이터를 주고받는 방식
    - **Get** : 데이터 조회
    - **Post**: 데이터 추가, 등록
    - **Put** : 데이터 업데이트
    - **Delete**

## Fast API
>**Pytho**n으로 **RESTful API**를 쉽게 구축할 수 있도록 도와주는 프레임워크

```py
# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "hello test"}

# uvicorn main:app --reload
# 파일이름:실행할 기능 이름

# url/docs : API 문서 제공
# url/redoc : ReDoc 으로 문서화
```

## 환경 변수
- 운영체제에서 사용자나 시스템의 상태정보를 저장하는 변수
- 시스템 전반에 영향
- 프로그램 실행 시 필요한 설정 정보 제공

### Path
- 실행 파일이 위치한 디렉토리 저장
 
### Home
- 사용자의 홈 디렉토리 지정

[¶ Top](#api--gemerative-model-use)

## API 관리

### Shell 설정 파일
- 사용자가 **Shell** 환경 커스터마이즈
- 영구적인 환경 변수 설정
- **zsh** : **zshrc**
- **API Key**를 등록해서 애플리케이션이 작동할 떄 호출 
- **Python** 코드로 호출
  - `import os`
  - `api_key = os.environ.get("본인의_API_키")`

```bash
vim ~/.zshrc # vim : 편집기, nano, code 등 다른 편집기도 가능
# i : 작성모드 -- INSERT --
# esc : 작성모드 종료
# : -> wq 입력 -> 엔터 : 저장 후 종료
# : -> q! 입력 -> 엔터 : 저장하지 않고 종료

export OPENAI_API_KEY="본인의_API_키" 
# API Key 등록
# 제일 밑에 줄 
source ~/.zshrc 
# 변경 사항 바로 적용
# 작성하지 않고 터미널 재시작 하면 적용
echo $OPENAI_API_KEY
# 확인
```

### .env 파일
- **API Key** 같은 민감정보를 저장한 뒤 로드해서 사용
- 여러 환경에서 코드와 환경변수를 쉽게 관리 가능
- 버전 관리 시스템에서 제외시켜야 함

### Secret Management Service
- 클라우드 비밀 관리 시스템
- 높은 수준의 보안
- 키 관리 자동화 기능

### CI, CD 시스템
- 배포 파이프 라인에서 민감 데이터 보호
- 자동화 배포 프로세스에 포함되어 실수가 적음

### **API Key** 를 암호화
- 애플리케이션 시작 시에 해독

# 생성형 모델 활용

## GPT-4o

## ElevenLabs API
> 텍스트를 자연스러운 음성으로 합성하는 서비스 제공

### 음성
- 사전 학습된 모델
- 사용자의 목소리 사용 가능
  - 모델 유출 시 보이스 피싱 등에 악용될 가능성
  - 대략 시간 단위의 목소리 데이터 필요
  - 음성 데이터와 사용자의 목소리를 비교하는 검증 단계 필요

### Pydub
- 음성을 학습하는 기능과 관련된 패키지

## Ultralytics YOLO
> **You Only Look Once** 모델 : 실시간 객체 탐지 분양에서 널리 사용, 높은 정확도와 빠른 속도

### 특징
- 속도 : 전체 이미지 한번에 처리하여 빠른 속도
- 정확도 : 여러 객체가 있는 복잡한 이미지에서도 높은 정화도로 객체 탐지
- 다양한 크기 : 다양한 크기의 이미지와 객체를 처리

### 객체 탐지 모델
- 이미지 속의 객체의 위치와 클래스를 동시에 예측
- ***이미지 전체를 한번에 탐지***
  - 단일 신경망(한번에 예측)
  - end to end(객체 탐지-분류가 한번에 이루어짐)
  - 전역 분석

``` 
S x S 크기의 그리드 셀(각 그리드 셀 중 한개만 객체 포함)
B 개의 경계 상자 
- 중심 좌표(x,y) 
- 상대 크기(w,h)
- cofindence(상자의 정확도-상자가 객체를 포함할 확률)
C 개의 클래스에 대한 확률 분포 예측

각 그리드 셀 : 각 경계상자 컨피던스 점수 x 클래스 확률 
최종점수 계산 -> 점수가 높은 상자 최종 예측
non-Maximum suppression 통해 여러개의 상자가 하나의 객체 탐지하는 경우 중복 제거
```

- 저작권 문제로 버전 사용에 주의가 필요

### 예시
- 다양한 형태의 `image_path` 를 입력해도 대응 가능
  - 예시 CCTV 객체 탐지

```py
# pip install ultralytics

from ultralytics import YOLO
import cv2
from matplotlib import pyplot as plt

model = YOLO('yolov8n.pt')

image_path = '/Users/yeongung/AI/cats.jpg'

results = model(image_path)

result = results[0]

img_with_boxes = result.plot()

plt.imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
```

![결과](/Tools/images/yolo_result1.png)

[¶ Top](#api--gemerative-model-use)