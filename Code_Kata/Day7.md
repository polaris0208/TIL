# 문자열 제거
```py
def solution(my_string, letter):
    a = my_string
    b = a.replace(letter, '')
    answer = ''.join(b)
    return answer
#
def solution(my_string, letter):
    return my_string.replace(letter, '')
```
# 각도기
```py
def solution(angle):
    a = angle
    if a == 90: answer = 2  
    elif a < 90 and a > 0: answer = 1
    elif a > 90 and a < 180: answer = 3
    elif a == 180: answer = 4
    return answer
#
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 
```
# 양꼬치
```py
def solution(n, k):
    lamp = 12*n
    coke = 2*k
    service = n//10
    receipt = (12*n + 2*k) - (2*service)
    answer = 1000*receipt
    return answer
    #
    def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)
```
# 짝수의 합
```py
def solution(n):
    even = []
    for _ in range(1,n+1):
        if _ % 2 == 0: even.append(_)
    answer = sum(even)
    return answer
#
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
```
