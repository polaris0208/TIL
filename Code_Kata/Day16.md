# 숫자 찾기

```py
def solution(num, k):
    num = str(num)
    k = str(k)
    n = list(num)

    for _ in n:
        if k not in n:
            return -1
        else:
            return n.index(k) + 1
```

# n의 배수

```py
def solution(n, numlist):
    answer = []
    for _ in numlist:
        if _ % n == 0:
            answer.append(_)
    return answer
```

# 자릿수 구하기

```py
def solution(n):
    n = list(str(n))
    answer = 0
    for _ in n:
        answer += int(_)
    return answer
```

# OX 퀴즈

```py
def solution(quiz):
    answer = []
    for _ in quiz:
        a = int(_.split()[4])
        q = ''.join(_.split()[0:3])
        if a != eval(q) : answer.append('X')
        elif a == eval(q) :answer.append('O')
    return answer 
```