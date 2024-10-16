## Python

### collection 데이터

1. list 
```
# [] 사용, 다양한 형태의 데이터를 요소로 포함 가능
```
* [0] #첫 번째 데이터에 접근
* len(리스트) # 리스트 길이 확인
* .remove # 제거, .append # 추가
* 첫 번째 요소 변경 # 리스트[0] = "변경"
* .sort() # 정렬

2. tuple 
```
#() 사용
```
* 리스트와 유사함, 조회에 사용하는 대부분의 기능 그대로 사용가능
* 불변 자료이기 때문에 데이터를 변경할 수 없음

3. dictionary 
```
# {} 
```
* key : value 조합으로 사용
* del dict(key) # 삭제
* dict.keys() # key 확인
* dict.values() # value 확인

4. set # {} 사용, key가 없음
* 중복 데이터 자동으로 없애줌
* .add, .remove

### 제어문과 반복문

1. 조건문 
```
# 주어진 조건에 따라 프로그램이 결정
```
* if 조건:
(들여쓰기)실행할 코드
* else:
(들여쓰기)실행할 코드(모든 조건이 거짓일 때)
* elif 다른 조건:
(들여쓰기)실행할 코드(다른 조건) # 조건 검사는 순차적으로 이루어지기 때문에 조건 설정에 유의
* .upper(), .lower() # 대문자 변환, 소문자 변환

2. 반복문
* for문 # 데이터들을 순차적으로 순회하면서 코드 실행
* while: # 참인 경우만 반복 / 초기선언조건문 
_거짓이 되는 부분을 설정 해주지 않으면 무한히 반복_

```python
age =18
while age < 20:
	print("미성년자 입니다.")
    age += 1    
```
   
* countinue 아래의 내용을 출력 하지 않고 다시 반복
* break 즉시 반복 정지
* range(시작, 종료, 단계): 실행할 코드 # 시작 기본값 = 0, 종료는 미포함, 단계 기본값 = 0

```python
for i, j enumerate(list_sample): 
	print(i,j) 
    # 위치, 값
```


### 함수

1. 내장함수(built-in)
* print() # 내부에 함수가 있는 경우에 연산이 먼저 진행된 후에 출력
* input() # 입력값은 문자열로 받기 때문에 가공 필요
* int(), float(), str() # int = 정수형, florat = 실수형
* sorted() # 기본 오름차순
* abs() # 절대값
* round(수, 반올림 할 자릿수) # 1 = 소수점 한자리로 반올림 ex) 3.14 -> 3.1

2. 함수 만들기
* 복습 : https://velog.io/@sh6771/TIL-Day-5-1
* retun 코드를 통해 얻은 값= 반환값
* *args 가변인자 # 튜플 형식으로 데이터 전달
* **kwargs 키워드 인자 # 딕셔너리 형식으로 데이터 전달

```python
def create_profile(name, age, *args, **kwargs):
	profile = { 
    	"name" : name,
        "age" : age,
        "intersets" : args,
        "etc" : kwargs
        }
    return profile
    
profile = create_profile("Alice", 15, "여행", city="원더랜드")
print(profile)
```
* *args, **kwargs  순서로 사용

3. 모듈
* 함수, 클래스, 변수를 하나로 미리 묶어놓은 것
* 모듈 불러오기 : import
* from 모듈 import 함수 # 전체는 *

_이름 충돌 주의
모듈 탐색 경로 설정 주의_

4. 패키지 
* 모듈을 묶어놓은 단위
```py
_init_.py #패키지를 초기화하는 파일(필수)
  module1.py
  module2.py
```
* 터미널을 이용한 설치

```bash
pip # 패키지 설치 및 관리
pip install 패키지
pip install 패키지==버전번호
pip install --upgrade 패키지 
pip uninstall 패키지
pip list
pip cache purge
```

5. 가상환경
* 패키지 설치 등으로 인한 충돌방지
* 따로 가상환경을 만들어 패키지를 설치하고 테스트

```bash
python -m venv 가상환경이름
# 가상환경 생성
# venv = virtural environment
source 가상환경이름/bin/activate
# 가상환경실행
# deactivate : 비활성화 명령어


```
6. 터미널에서 Python 구동
* 명령어 python 입력

7. 터미널 명령어 참고
https://ko.appflix.cc/useful-collection-of-mac-terminal-commands-to-know/#mv-파일-폴더-이동-파일-이름-변경

#### 차후 확인 사항
1. 비트연산자 - 이진수 보수 개념 정립
2. 터미널 상에서 python 파일 호출하기
3. tuple  개념 정리
* 개념, 기능, 예시 - list, dictionary 와의 차이점을 중심으로