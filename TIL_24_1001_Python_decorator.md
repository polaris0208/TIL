## Python

#### Python 기호
* " * " - 모든 것
* 가변인자 - *args, **kwargs
* -> - 함수 정의
* ... - 생략부호, pass 처럼 사용 가능
* % - 문자열 포메팅 - %s 문자, %d 정수, %f 소수
```python
fruits = ["사과", "딸기", "배"]
cnt = 1
for fruit in fruits:
  print (" %s %d" %(fruit, cnt), "개")

# "%타입" %(타입인수) 구조
#  인수가 한개인 경우 ()생략
  
# 사과 1 개 딸기 1 개 배 1 개

```
* @ - decorator 기능

### Decorator
* 함수를 수정하지 않고 기능을 추가
* 함수를 감싸는 형태 -> wrapper

```python
def deco(origin):
  def wrapper(): # wrapper 함수로 원본 함수를 감싸 내용추가
    print("비오네☔️🌧️...")
    origin()
    print("징징징🎸🎸🎸~ ")
  return wrapper # wrapper 함수를 반환

@deco
def origin():
  print("IU - Bye Summer")

origin()

# 
비오네☔️🌧️...
IU - Bye Summer
징징징🎸🎸🎸~ 

```
### Iterator
* 반복 가능한 객체를 하나씩 꺼냄
```python
numbers = [1,2,3,4,5] #리스트
iterator = iter(numbers) 
next(iterator) #next() 메서드로 호출
# 1
next(iterator)
# 2

```

* class 적용 예
```python
class myiterator:
  def __init__(self, data):
    self.data = data
    self.index = 0 #.index = 원소의 위치

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.index < len(self.data):
      result = self.data[self.index]
      self.index += 1
      return result
    else:
      raise StopIteration 
      #raise : 에외 설정(버그 대비) stopIteration - 정지
      
 my_iter = myiterator([1,2,3])
 for a in my_iter:
  print(a)
 # 1 2 3
```
### Generator
 * generator는 iterator를 생성
 * 단 모든 값을 한번에 생성하지 않고 필요할 때 생성
 * yield 키워드를 사용하여 값을 하나씩 변환
 
```python
[1,2,3,4,5]

 def generate_5(): 
  yield 1 
  yield 2
  yield 3
  yield 4
  yield 5
  
gen = generate_5()
next(gen)
# 1
```
* 피보나치 수열 만들기
```python
def fibonacci(n):
  a, b = 0, 1
  for _ in range(n): 
  #의미 없는 변수 _ 사용 
  https://dkswnkk.tistory.com/216
    yield a #generator
    a, b = b, a + b
    
for num in fibonacci(10):
  print(num)

# 0 1 1 2 3 5 8 13 21 34
```
### 파일 다루기
* f : file
* r : 읽기 / w : 쓰기 / a : 추가하기
```python
f = open("/Users/유저명/bye_summer.txt", "r")
# 우클릭 - alt - 경로 이름 복사
line = f.readline() # 한줄만
print(line)
f.close # 파일 닫기

# while True: 
  line = f.readline()
  if not line: break
  print(line)
f.close
# 비오네☔️🌧️... 
```
* 한 줄씩 전체
```python
while True: # 값이 True인 동안 반복
  line = f.readline() # 한 줄씩
  if not line: break
  print(line)
f.close

#비오네☔️🌧️... ~(생략) 서늘한 바람이.. 💨💨💨🌪️🌬️

```
* 파일 전체(줄)
```python
for line in f:
  print(line)
f.close
```
* 여러줄
```python
lines = f.readlines() #readline 아닌 lines
for line in lines: # 전체
  line = line.strip() #.strip 공백없이
  print(line)
f.close
```
* 파일 전체 읽기
```python
data = f.read() #f.read() 읽기
print(data)
f.close
```
* 내용 추가하기 (context manager)
```python
with open("/Users/유저명/bye_summer.txt", "a") as f:
# with 구문을 사요하면 f.close 생략 가능
  f.write("IU - Bye Summer") # f.write() 쓰기
  
# 다시 데이터를 읽으면 마지막 부분에 "IU - Bye Summer" 추가됨
```

#### 차후 확인 사항
1. 리스트 만들기, 제너레이터 표현식 
2. Python Library 개념 + Frame work
