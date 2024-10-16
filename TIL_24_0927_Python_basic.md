## Python 기초


_작성은 top to bottom_

1. variable - 데이터 명명, 명명된 이름으로 데이터에 접근

* camel case - myAge = javascript에서 주로 사용
* snake case _ my_age = python 
* 숫자만 사용하는 것은 지양, 문자로 시작하되 숫자를 섞는 것은 가능

2. 문자
* "" 사용

3. True, False
* T, F 는 항상 대문자

4. print()
* print("Hello my name is", my_name)

### function
* def 을 통해 정의
* (): 사용

```py
def say_hello():
   print("hello how r u?")

say_hello()
```

6. 공백의 사용 - python의 특징
* 두 칸 들여쓰기 - 코드 포함
* tap 1번 클릭 or space 2번 클릭

7. function 커스터마이즈

```py
def say_hello(user_name):
  print("hello", user_name, "how r u?")

say_hello("name")
```

* user_name = parameter(매개변수), name = argument(전달인자)
* parameter 와 argument는 여러개 사용 가능하며, 이 때는 개수와 순서에 맞춰 작성

```py
def say_hello(user_name, user_age):
    print("hello", user_name)
    print("you r", user_age, "years old")

say_hello("name", 28)
```

* 연산에 parameter 활용 
* 거듭제곱 연산 = ** , power / 2제곱 = square_

```py
def tax_calculateor(salary):
    print(salary*0.35)

tax_calculateor(100)
```
* paramete에 기본값 설정

```py
def say_hello(user_name="everyone"):
  print("hello", user_name)

say_hello()
```

### return
* 함수 밖으로 값을 보냄

```py
def tax_calc(money):
  return money*0.35

def pay_tax(tax):
  print("thank you for paying", tax)
  
pay_tax(tax_calc(100000000))
```

* f-string

```py
print(f"hello I'm {my_name}")
```
* return 활용

```py
def make_juice(fruit):
  return f"{fruit}+juice"

def add_ice(juice):
  return f"{juice}+ice"

def add_sugar(iced_juice):
  return f"{iced_juice}+sugar"

juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

# apple+juice+ice+sugar
```

_return은 함수의 끝(이후 값은 전달 x)_