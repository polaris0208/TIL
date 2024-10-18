# 피자 나누기 1
```py
def solution(n):
    if n % 7 == 0:
     answer = n // 7
    elif n % 7 != 0:
     answer = n // 7 + 1
    return answer
#
def solution(n):
    return (n - 1) // 7 + 1
```
# 피자 나누기 2
```py
def solution(n):
    pizza = 6
    while pizza % n != 0:
        pizza +=6
    answer = pizza//6
    return answer
#
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
```
# 피자 나누기 3
```py
def solution(n):
    pizza = 6
    while pizza % n != 0:
        pizza +=6
    answer = pizza//6
    return answer
#
def solution(slice, n):
    return ((n - 1) // slice) + 1
```
# 배열의 평균
```py
def solution(numbers):
    sum_ = sum(numbers)
    count_ = len(numbers)
    answer = sum_ /count_
    return answer
#
def solution(numbers):
    return sum(numbers) / len(numbers)
```