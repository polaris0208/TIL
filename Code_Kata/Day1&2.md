## 나의 풀이 # 다른 사람의 풀이
1. 두 원소
```py
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        p = num_list[-1] - num_list[-2]
    else:
        p = num_list[-1] * 2
    num_list.append(p)
    return num_list

# 
def solution(num_list):
    a = num_list[-1]
    b = num_list[-2]
    if a > b:
        num_list.append(a-b)
    else:
        num_list.append(2*a)
    return num_list
```
2. a와 b 출력하기
```py
print(f'a = {a}\nb = {b}')
#
print("a =",a) 
print("b =",b)
```
3. 두 수의 합
```py
def solution(num1, num2):
    num1 + num2
    return num1 + num2
#
solution=lambda *x:sum(x)
```
4. 두 수의 차
```py
def solution(num1, num2):
    answer = num1 - num2
    return answer
#
solution = lambda num1, num2 : num1 - num2
```
5. 두 수의 곱
```py
def solution(num1, num2): 
    answer = num1*num2
    return answer
#
def solution(num1, num2):
    #return num1 * num2
    i = 0
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer
```
6. 두 수의 몫
```py
def solution(num1, num2):
    answer = num1 // num2
    return answer
#
solution = int.__floordiv__
```
7. 나누기
```py
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer
# 동일
```
8. 제어문
```py
def solution(num1, num2):
    if num1 == num2 : answer = 1
    else: answer = -1
    return answer
# 동일
```
9. 분자와 분모
```py
import math
def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    
    t = math.gcd(a, b) 
    
    answer = ((a/t),(b/t))
    return answer
# 동일
```
10. 배열
```py
import numpy as np

def solution(numbers):
    num = np.array(numbers)*2 
    answer = num.tolist()
    return answer
#
def solution(numbers):
    return [num*2 for num in numbers]
```