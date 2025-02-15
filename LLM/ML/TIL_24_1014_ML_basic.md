## ML 기초
> Machine learning 기본 개념
> Pandas 데이터 전처리 복습
> 회귀모델(regression)
> 분류모델(classification)

### Machine learning 기본 개념
#### 1. 머신러닝
```
ai 알고리즘의 일부
ai - 컴퓨터가 스스로 사고하는 것
```
* 명시적으로 프로그래밍되지 않아도 데이터를 통해 학습하고 예측(딥러닝은 조금 더 세부적인 영역)
*  지도학습, 비지도 학습, 강화 학습 등 - 계층을 구성하면 딥러닝
* 데이터로 부터 패턴을 분석하고 학습하여 규칙과 논리를 찾을 수 있는 프로그램 

#### 2. 머신러닝의 대두
* 알고리즘 자체는 1980-90s에 등장
* 데이터의 증가, 컴퓨팅 파워의 향상, 연구로 인한 알고리즘의 발전, 오픈소스

#### 3. 머신러닝의 개요

* 지도학습(정답포함)
-데이터셋 ex) 위치, 평수 -> 집값(정답)

* 비지도 학습(정답이 없음, 묶기)
-fearute(특징) ex) 사과, 오렌지, 배....-> 특징들로 묶기 clustering

* 강화 학습(순차적인 결정문제)
-action(특정행위) ex) 알파고-데이터를 행동의 근거로 사용

#### 4. 머신러닝의 구성

* 데이터 셋 :머신 러닝의 베이스
        입력 데이터 : feature: 모델이 학습할 수 있는 개별 속성 - 정답을 추론하기 위한 정보들
        출력 데이터 : label(정답) - 비지도 학습에는 없음, 정해진 것이 아니라 문제에 따라 달라짐 

* 모델: 데이터 feature 로부터 label을 예측 할 수 있는 지식을 학습하는 프로그램/함수
        overfiting - training data set 만 과도하게 학습 - 일반 지식에 대응 불가

* 학습 : 데이터로부터 규칙과 논리를 배우는 것 
      과정 - training- 모델마다 다름

* 학습 과정
```
    데이터 수집 -> 데이터 전처리 -> 특징 선택 -> [모델 선택 -> 모델 훈련 -> 모델 평가] -> 모델 배포  
                                           <---      cycle     --->
```                                          
```
 feature 선택 - feature engineering : 중요한 것 선택, 불필요한 것을 제거하는 과정(성능에 크게 영향)
 feature 결합 - tuning - 가로길이 데이터, 세로길이 데이터를 결합해서 크기 데이터로 활용
 모델 선택 - 특징 선택에 따라 기준이 달라짐 
 모델 훈련 - 학습
 모델 평가 - 평가 : 학습에 사용한 데이터는 사용 불가(100개 중 80개 학습, 20개는 테스트)
```

#### 5. 학습 방법
  * 지도학습(supervised learning) - 레이블이 있는 데이터 셋
                              - 회귀(regression) 연속적인 값 예츠
                              - 분류(classification): 이산적인 값 예측
                              <br>
  * 비지도 학습(un,,) - 군집화(clustering) - 데이터를 유사한 그룹으로 묶음
                  - 차원 축소(dimensionality reduction) - 고차원 데이터를 저차원으로 변환
                  <br>
  * 앙상블 학습(ensemble learnong): 여러개의 모델을 결합하여 더 나은 성능
                  - 배깅(bagging) : 여러 모델을 독립적으로 학습싴고 예측을 평균내거나 다수결 투표로 최종 예측
                  - 부스팅(boosting) 여러 모델을 순차적으로 학습- 이전 모델의 오차를 보완해 나가면 최종 예측
                  - 스태킹(stacking): 여러 모델의 예측 결과를 새로운 데이터로 사용하여 메타 모델을 학습

### Pandas 데이터 전처리
#### kaggle 데이터 활용
* api 발급
```bash
프로필 - 세팅 - api - jason 파일 디렉토리에 저장
(~/.kaggle/kaggle.jason)
```
* .kaggle 폴더가 없는 경우
```bash
kaggle competitions download -c 대회이름- 코드입력
# api가 없다는 에러 발생 이후 .kaggle 폴더가 생성됨
```
* kaggle 데이터 불러오기
```bash
불러올 폴더로 이동 cd /Users/사용자이름/myenv/studynote/kaggle
kaggle competitions download -c 대회이름
unzip 대회이름.zip

train_df = pd.read_csv('/Users/사용자명/myenv/studynote/kaggle/train.csv')
# 파일경로= kaggle 폴더 csv 파일 우클릭-path copy
```
#### 데이터 전처리
* data cleaning / 원시 데이터 raw data는 형식이 일관되지 않음
```
# 결측치 처리 - 누락된 데이터 처리 -삭제 , 대체 , 예측 
# 이상값 처리 - IQR : 이상치 탐지(특정 값을 정해놓고 넘어가면)
# 중복 데이터 처리 - 데이터의 불균형, 데이터 가중치 문제 해결
# 터압 변환 - 모델이 사용 가능한 타입
# 데이터 표준화 - 데이터의 평균과 분산을 변환(각각 0,1)
# 특성 공학 - 데이터로부터 유용한 특성을 생성하는 과정
# 데이터 인코딩 - 비선형 데이터를 모델이 이해할 수 있는 형태로 변환
            # 레이블 인코딩(숫자), 원-핫(이진법)
# 데이터 분할 - 학습 데이터, 검증 데이터, 테스트 데이터 
```
* 주요 기능 예시
```py
# 행제거 0, 열제거 1
df.dropna(axis=1)  
# 중복값 확인
df.duplicated().sum()
# 타입 변환
df['C'].astype(float)
# one-hot
df_encorded = pd.get_dummies(df, columns=['category_column'])
# 샘플링
df_sampled=df.sample(frac=0.5) # 50퍼 # n=100(개)
```
### IQR 이상치 처리
* IQR(Inter Quantile Range) : Quantile 사이의 범위 ; 
이상치 처리에서는 25-75% 사이 범위
* Quantile이란 주어진 데이터를 동등한 크기로 분할하는 지점
이상치 처리에서는 25% 단위
```py
Q1 = df['column_name'].quantile[0.25] # 75% 지점
Q3 = df['column_name'].quantile[0.75] # 25% 지점
IQR = Q3 - Q1 # 범위 
# 1.5 오차범위를 곱하여 최소 최대 값을 구함
lower_bound = Q1 - 1.5 * IQR # 최솟값
upper_bound = Q3 + 1.5 * IQR # 최댓값
```
```html
<lb --Q1 ---Q2(중간값)---Q3-- ub>
최솟값과 최댓값을 벗어나는 범위를 이상치로 판단
```
* 이상치 제거, 대체
```py
# 이상치 제거
df_no_outliers = df[(df['column_name'] >= lower_bound) &
									(df['column_name'] <= upper_bound)]

# 이상치를 평균값으로 대체
mean_value = df['column_name'].mean()
df['column_name'] = df['column_name'].apply(
			lambda x: mean_value if x < lower_bound or x > upper_bound else x)
```
## 지도 모델(Supervsed Model)
### 선형회귀(Linear Regression) 
* 독립변수 - 예측하기 위해 사용되는 변수
* 종속변수 - 예측하는 변수
* 선형관계 = 직선으로 관계를 예측 할 수 있다
(독립 변수가 1개 - 단순선형 / 여러개 - 다중선형)
```
학습 : loss function(목적 함수)를 최소화하는 독립변수(B)를 찾는 것
목적함수 : 예측값과 실제값의 오차
방법 : 미분(경사하강법) 또는 최적화 함수
```
* 복잡하기 떄문에 여러 단계에 걸쳐 찾는다
* Global optimum: 오차가 최소가 되는 지점
* Local optimum: 최적점 처럼 보이는 지점
주의점: 모델이 여기가 최점적이라 판단하고 수렴해버리는 경우
```py
import numpy as np # 연산 
import pandas as pd # 데이터 처리
from sklearn.model_selection import train_test_split # 데이터 분할
from sklearn.linear_model import LinearRegression # 선형 모델의 선형 회귀
from sklearn.metrics import mean_squared_error, r2_score # 성능 평가
```
* 모듈 import, 데이터셋 준비
```py
X = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5],[6,6]]) # 독립변수
y = np.array([1, 2, 3, 4, 5, 6]) # 종속 변수
```
* 학습, 테스트 데이터 분할
```py
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# x 는 독립 변수, 테스트 사이즈 20퍼센트, random_state는 시드값, 시드값이 달라지면 결과가 달라짐
# 예시가 42인 이유는 더글러스 애덤스의 은하수를 여행하는 히치하이커를 위한 안내서의 궁극의 해답 42로 추측
```
* 선형 모델 선택, 학습 진행
```py
model = LinearRegression()
model.fit(X_train, y_train) # 테스트 데이터와 테스트 정답 - 학습 진행
```
* 예측, 레이블 확인
```py
y_pred = model.predict(X_test) # 예측
y_pred # array([1., 2.])
X_test # array([[1, 1], [2, 2]])
```
* 평가모델
```py
mse = mean_squared_error(y_test, y_pred) # 0에 근접할 수록 우수
r2 = r2_score(y_test, y_pred) # 1에 근접할 수록 우수
```
### 다항회귀(Polynomial Features)
* 곡선, 비선형 관계도 예측 가능
```
y= B0 + B1x + B2x제곱........(예측할 데이터를 늘려감 )
```
* 적절한 차수를 정하는 것이 중요
* overfitting 과적합 문제
```py
from sklearn.preprocessing import PolynomialFeatures # 다항회귀 # 차수선택
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([1, 4, 9, 16, 25, 36])
```
* 데이터 변형
```py
poly = PolynomialFeatures(degree=2) # 2차항까지
X_poly = poly.fit_transform(X) # 데이터 전달
X_poly # 0차항, 1차항, 2차항
```
* 나머지 과정 선형과 동일
* 다항회귀도 선형회귀로 간주(가중치와 독립변수의 선형적 결합), 단지 더 복잡한 값을 넣어 성능을 향상
```py
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```
### Logistic 회귀
* 분류 모델(둘 중 하나로 분류)
* 종속변수가 이진형일때-결과가 둘중 하나 일때
<br>
* 시그모이드 함수(sigmoid)
결과값이 0과 1사이에 위치 - 데이터가 클래스에 속할 확률을 예측
<br>
* 비용함수(모델의 예측확률과 실제 레이블 사이의 차이르 측정)
#로그 손실 함수 - 크로스 엔트로피 함수

```py
from sklearn.datasets import load_breast_cancer # 데이터 셋 가져오기
from sklearn.preprocessing import StandardScaler # 표준화 도구
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```
* 기본 (판다스, 넘파이, train_test_split) + 추가모듈
```py
# 데이터 로드
data = load_breast_cancer()
X = data.data 
y = data.target # 레이블 # 이진데이터

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 스케일링
scaler = StandardScaler() # 평균이 0 분산 1
X_train = scaler.fit_transform(X_train) # 평균과 편차를 찾아서 정규화
X_test = scaler.transform(X_test) # fit 제거 -테스트 데이터의 평균과 편차를 사용하면 안됨

# 모델 생성 및 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```
### SVM 분류모델 (Support Vector Machine)
* 차원에 따라 가장 잘 나누는 선 또는 면을 찾는다 
* 분류와 회귀분석에 사용
```
결정경계(결정 초평면 ,2차원 이상일 떄 hyperplane)
 - 두 클래스 사이의 최대 margin을 보장 
 - margin : 두 클래스의 가장 가까운 데이터의 거리
 - 서포트 백터 결정 초평면에 가장 가까이 위치한 데이터 포인트=결정경계를 정의

커널 함수
 - 데이터를 더높은 차원으로 매핑하여 선형적으로 분리할 수 없는 데이터를 분리
```
* 모듈 import
```py
import numpy as np # 연산 
import pandas as pd # 데이터 처리
import seaborn as sns
from sklearn.model_selection import train_test_split # 데이터 분할
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC # 오류 처리 방식에 약간 차이가 있는 svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```
* 데이터 처리
테스트 데이터에는 fit.transform을 사용하지 않는다(맞춰진 데이터에 테스트 하면 의미x)
```py
# 데이터 로드
titanic = sns.load_dataset('titanic')

# 필요한 열 선택 및 결측값 처리
titanic = titanic[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']].dropna()

# 성별과 탑승한 곳 인코딩
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic['embarked'] = titanic['embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# 특성과 타겟 분리
X = titanic.drop('survived', axis=1)
y = titanic['survived']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
* 모델 생성 - 학습
```py
# 모델 생성 및 학습
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```
### KNN 분류모델(K Nearest Neighbor)
* 분류모델
* 알고리즘과 유사
* 학습데이터를 기반으로 새로운 데이터 포인트의 클래스를 예측 
* 데이터를 펼쳐낸 후 거리를 계산하여 가장 가까운 이웃을 차음
* 거리측정과 k값이 중요 : 거리는 진짜 거리, k 값은 정하기 나름
```
# 예시
# k=1 거리 내의 보라색 1개 = 보라색로 판단 가능
# k=2 거리 내에 보라색 1개 파란색 2개 = 파란색으로 판단 가능
```
* 이전까지 KVM과 동일
```py
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```
### Naive Bayes 분류 모델
* 분류 모델
* 통계 모델
* naive 각 feature가 독립적
* bayes 베이즈 정리 기반
```
조건부 확률
a = 우산
b = 비
p(a|b) b일때 a일 확률 = p(b|a)* ( p(a) / p(b) )
```
* 모델 개념
```
# 베이즈 정리
예시) 메일 - 스팸 메일

# 알고 싶은 것
 - 특가라는 단어가 있을 때 스팸메일 
# 알 수 있는 것 
 - p(스팸) 전체 메일 중 스팸메일 개수
 - p(특가) 전체 매일 중 특가 포함된 개수
 - p(특가|스팸) = 스팸일때 특가가 나올 확률 - 스팸메일에 특가가 포함된 경우

# 결과적으로 p(스팸|특가) = p(특가|스팸) * ( 스팸 / 특가 ) 
# 확률을 종합적으로 정리해서 추측 

# 나이브 개념(독립시행)
특가 + 평생 을 종합적으로 고려해서 적용하고 싶음
그러려면 두개가 독립적이어야 함 = 특가가 나올 떄 평생일 나오는 것이 상관관계가 없어야 함
```
* 모델 종류
* 확률의 곱셈으로만 연산 -> 연산이 복잡하지 않음
* 가우시안 - 정규 분포 가정 
* 베르누이 - 이진수 경우
* 멀티노미어 - 다항 분포 경우
<br>
* 이전까지 KVM과 동일

```py
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = GaussianNB()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```
### 의사결정나무(Decision tree)
* feature을 기준으로 의사결정 규칙을 만들고 이를 바탕으로 데이터를 분류하거나 회귀
* 규착에 따라 분류를 거듭하다 데이터가 충분이 작아지는 지점에 의사결정
* 학습 - 규칙을 학습하는 것
* 규칙 - 불확실성을 줄여주는 것
```
# 트리구조 
			    <root node>
                       no -  /       \ - yes
                      <leaf node>  <inernal node> 
                         branch(edge) - \ - yes
                                    <leaf node>                                
node - 데이터 특정 특징에 대한 테스트
branch(edge)- 테스트 결과
leaf - 클래스 레이블
```

* gain information - 엔트로피(불확실성)값으로 데이터를 나누는 기준
* gini 계수 - 불순도를 측정
<br>
* 이전까지 KVM과 동일

```py
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")
print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
```

