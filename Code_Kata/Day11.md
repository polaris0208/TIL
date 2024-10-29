# 주사위
```py
def solution(box, n):
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    return a*b*c
# 언팩 개념 
def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )
```
# 약수
```py
def solution(n):
    def measure(x):
        list_ = []
        for _ in range(1,x+1):
            if x % _ == 0:
                list_.append(x)
                list_.append(x//_)
        return len(set(list_))
    answer = 0
    for num in range(1,n+1):
        if measure(num) > 2: answer += 1
    return answer
#
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
```
# 최댓값
```py
def solution(numbers):
    sorted_num = sorted(numbers, reverse=True)
    answer = sorted_num[0] * sorted_num[1]
    return answer
#
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
```
# 팩토리얼 
```py
def solution(n):
    def fac(i):
        m = 1
        for _ in range(1, i+1):
            m *= _
        return m
    answer = []
    for x in range(1, n + 1):
        if fac(x) <= n : answer.append(x)
        elif fac(x) > n : break
    return max(answer)
#
def solution(n):
    answer = 1
    factorial = 1
    while factorial <= n:
        answer += 1
        factorial = factorial * answer
    answer -= 1
    return answe
```