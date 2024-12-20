## 과적합 방지 기법
> 정규화, Dropout, 조기종료, 데이터 증강
- 과적합 **Overfitting**
- 학습이 과도하게 진행되어 일반적인 문제 예측 불가
- 답을 완전히 외운 상태

### 정규화 **Nomalization**
1. 개념
- 데이터를 **일정한 범위**로 조정 
2. 종류
- 배치 정규화 **Batch Nomalization**
  - 각 미니배치에서 활성화 값을 정규화
  ``` 
  1. 미니 배치에서 특징의 평균과 분산을 계산
  2. 활성화 값은 평균과 분산을 이용해 정규화
  3. 재스케일링 및 시프트 
  - 학습가능한 파라미터 감마, 베타 사용
  - 값을 조정
  ```
  - 활성화 값: 활성화 함수를 통해 계산된 값
  - 미니배치: 적절한 크기로 나눠 모델을 업데이트
  - 장점
    - 학습이 빨라짐
    - 학습률을 더 크게 사용
    - 학습이 안정적이고, 초기화 값에 민강하지 않게 됨
    <br>
- 레이어 정규화 **Layer Nomalization**
  - 주로 RNN 사용
  - 각 레이어의 활성화 값을 정규화 
    - 순환하는 RNN의 특징으로 정규화가 일부 제한 떄문
  - 동작원리
  ```
  1. 각 레이어의 활성화 값을 확인
  2. 평균과 분산을 확인
  3. 이 값을 통해 정규화 진행
  4. 재스케일링 시프트
  ```
  - 배치 크기에 영향을 받지 않음 
    - 시퀀스 데이터에 적합
    <br>
- 그룹 정규화 **Group Nomalization** 
  - 배치 정규화와 레이어 정규화의 장점을 결합
  - 채널을 그룹으로 나누고 각 그룹에서 정규화
  <br>
- 인스턴스 정규화 **Instance Nomalization**
  - 각 샘플에 대해서 정규화

> 그룹 정규화와 인스턴스 정규화는 Advanced 모델
> 상세하게 공부한 후 사용
> 비전 작업, 스타일 변환, 생성 작업 등
### 드롭 아웃 **Dropout**
- 학습 과정에서 무작위로 뉴런을 **비활성화**
```
<과적합>
30 명의 학생
1명의 뛰어난 학생이 A존재 
모든 문제를 A가 해결하는 문제 발생
A가 모르는 문제는 해결 불가
<드롭아웃>
임의의 학생들에게 문제를 배정
학생 전체가 일반적인 지식을 학습
한 학생이 모르는 문제는 다른 학생들이 해결 가능하도록 함

```
- 평가 또는 실사용 시에는 모든 뉴런을 활성화

### 조기 종료 **Early Stopping**
- **학습 - 검증 - 평가** 데이터로 분할
- 검증 데이터를 통해 성능을 판단
- 검증 데이터의 성능이 더이상 오르지 않으면 중단

### 데이터 증강 **Data Augmentation**
- 원본 데이터를 변형하여 **새로운 데이터 생성**
- 데이터를 **다양화**
- 이미지와 같이 변형할 가능성이 많은 경우 효과적
``` 
<원본 데이터>
나는 - 고등학생 탐정 - 남도일
<변형 데이터>
나는 - 남도일 - 고등학생 탐정
<변형 데이터>
고등학생 탐정 - 나는 - 남도일
....
```
-----
## 하이퍼 파라미터 튜닝<br>**Hyperparameter Tuning**
> 모델 학습의 여러가지 설정값
> 설정에 따라 모델 성능에 영향



### 하이퍼 파라미터
1. 학습률 **Learining Rate**
- 가중치를 업데이트 시 **얼마나 학습할지** 결정 
- 일반적으로 0.1, 0.01, 0.001 등

2. 배치 크기 **Batch Size**
- 한번의 업데이트에 사용하는 데이터의 샘플 크기
- 일반적으로 2의 배수꼴
- 32, 64, 128

3. 에포크 **Epoch**
- 데이터를 반복해서 학습하는 **한 주기**
- 10 에포크 = 주기를 10회 
- 조기 종료 기법을 사용하여 적절하게 결정 가능

4. 모멘텀 **Momentum**
- 이전 기울기를 현재 기울기에 반영
  - 학습 속도를 높이고, 진동의 줄임
- 일반적으로 0.9, 0.99 등
- 최적화 방법 설정에 사용
  - 학습결과를 바탕으로 가중치를 어떻게 업데이트할지 결정
```
경사하강법: 손실함수를 최소화
- 모델의 가중치를 반복적으로 업데이트
- 각 업데이트는 손실함수의 기울기를 보고 미분적으로 진행
```
- **Batch Gradient Descent**
  - 전체 데이터 셋 활용 
  - 한번에 가중치를 업데이트
- **Stochastic Gradient Descent**
  - 데이터 샘플을 사용
  - 가중치 업데이트가 균일하지 못함
  - 손실함수 진동 가능
- **Mini Batch Gradient Descent**
  - 데이터 셋을 작은 배치로 나눠서 사용
  - 효율성과 안정성

- **AdaGrad**
  - 자주 등장하는 특징은 학습률을 줄임
  - 드물게 등장하는 특징의 학습률을 늘림
  - 학습이 장기화 되면 학습률이 줄어드느 문제 방생

- **RMSProp**
  - 최근의 기울기를 기반으로 학습률을 조정
  - AdaGrad 단점 보완
  - 자체적인 하이퍼파라미터가 많아 설정이 복잡힌 문제

- **Adam**
  - 모멘텀과 RMSProp의 장점을 결합
  - 학습률을 동적으로 조정
  - 빠르고 안정적
  - 하이퍼파라미터가 많아 설정이 어려움

4. 가중치 초기화 **Weight Initialization**
- 모델의 가중치를 초기화하는 방법을 결정
- **Xavier** 초기화
  - 입력 노드의 수를 고려
  - **Sigmoid**, **Hyperbolic Tangent**활성화 함수 사용하는 경우
- **He** 초기화
  - 입력과 출력 노드의 수를 고려
  - **ReLU** 함수 사용하는 경우

### 자동 튜닝 기법
1. **Grid Search**: 모든 조합을 시도

2. **Random Search**: 무작위 값을 선택

3. **Bayesian Optimization**: 이전 평가 결과를 바탕

----
## 모델 평가와 검증<br>**Validation**
> 교차 검증 방식
### 개념
- 교차검증 **Cross-Validation**
  - 모델의 성능 평가
  - 데이터를 여러번 나누어 학습과 검증을 반복
- 필요성
  - 과적합 방지
  - 일반화 성능 평가
  - 데이터 효율성
### K-Fold 교차 검증
1. 원리
- 데이터를 k개의 폴더로 분리
- 각 폴드가 한번씩 검증 데이터로 사용
- 나머지는 학습 데이터
- 검증 결과를 평균하여 모델을 평가
2. 적용방법
- 각 폴드에 대한 검증 결과 저장
- 저장한 결과를 평균하여 성능 평가
----