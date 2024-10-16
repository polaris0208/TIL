## OOP

#### class 는 object를 만들기 위한 template 즉 설계도

```python
class 클래스:
	def __init__(self, 속성A, 속성B):
    	self.속성A = 속성A,
        self.속성B = 속성B
        
인스터스 = 클래스("A", "B")

# 클래스라는 틀을 이용해 속성A, 
# 속성B에 대응하는 속성, A, B를 가지는 객체 생성
```
### magic method
* init 생성자, 초기화
* repr 공식적인 문자열 반환
```
# 그대로 사용했을 때 동일한 객체 생성하는 문자열을 반환해야한다.
# 주로 디버깅에 상용
```
* add 객체간의 덧셈(문자열도 가능)
* eq 두 객체가 같은지 비교
* str  비공식저인 문자열 반환

```
# 보여지기 위한 문자열
# 사용자가 보기 좋은 문자열
```
#### class method
* 클래스 단위로 사용

```python
calss myclass:
	class_variable = 0
    
    @classmethod 
    def increment(cls): 
    cls.class_varible += 1
    
myclass.increment()
print(myclass.classvariable)

# 1 
# 한번 더 실행하면 2

a = myclass
a.class_variable

# 2
# 클래스 내부에서 값이 변경 되었기 때문에 생성된 객체인 a에서도 값을 공유
```

#### static method
* 정적 메서드
```python
# 클래스나 객체의 상태와 상관없이 정의
clss utility:
	@staticmethod
    def add(x, y)
    	return x + y
result = utility.add(2, 3)
print(result)
# 5
```
### 상속(inheritance)
* 부모 클래스에게서 속성과 메서드를 물려받아 공유
```python
class animal: # 상위 클래스 생성
  def __init__ (self, name): # 속성부여
    self.name = name

  def speak(self): # 메서드 생성
    return "소리를 냅니다."
    
class dog(animal): # 하위 클래스 생성
  def speak(self): # 상속받은 메서드 사용
    return f"{self.name}가 멍멍 짖습니다."
  # 오버라이드 하여 새로운 기능 추가
  
my_dog = dog("Brandon")
print(my_dog.speak())

#Brandon가 멍멍 짖습니다.
```
* 부모 클래스 초기화
```python
super().__init__()

부모 클래스의 매서드를 자식 클래스에서 실행

class dog(animal):
  def __init__(self, name, age):
    super().__init__(name) #animal의 메서드
    self.age = age
  def speak(self): 
    return f"{self.name}가 멍멍 짖습니다."
  
my_dog = dog("Brandon", 0.1)
print(my_dog.speak()
```
