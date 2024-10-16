## Python 기초

### 조건문

```py
password_correct = False

if password_correct:
  print("Here is your money")
else : 
  print("Worng password")
```
* if, else, elif
* if 조건 : 결과
* else: 대안
* elif 다른 조건: 대안
* 상단의 조건이 충족되면 아래의 조건이 충족되어도 출력되지 않음

_같다 ==, 다르다 !=, =은 값을 나타낼 때, ==은 값을 비교할 때_

2. input
* 입력값을 return값으로 사용

3. type
* variabl의 타입을 설명

4. int
* 문자형으로 표현된 숫자를 정수형 숫자로 변환

```py
age = int(input("how old are you?"))

if age < 18:
  print("You can't drink.")

elif age >= 18 and age <= 35:
  print("You drink bear!")

else: 
  print("go ahead")
```

5. python standard library 
* built_in_functions 기본 포함된 함수들 ex) print, int....
* 나머지 함수들은 필요에 맞게 적용해서 사용

```py
from random import randint, uniform
```
* random 모듈에서 randint, uniform 함수 불러오기

```py
user_choice = int(input("Choose number."))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
  print("You won!")

elif user_choice > pc_choice:
  print("Lower!", pc_choice)

elif user_choice < pc_choice:
  print("Higher!", pc_choice)
```
* randint 적용하여 무작위 정수값 출력