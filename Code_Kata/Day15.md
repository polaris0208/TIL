# 편지
```py
def solution(message):
    return 2*len(list(message))
#
def solution(message):
    return len(message)*2
```

# 가장 큰 수
```py
def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer
#
def solution(array):
    return [max(array), array.index(max(array))]
```

# 문자열 계산
```py
def solution(my_string):
    answer = eval(my_string)
    return answer
```

# 유사도
```py
def solution(s1, s2):
    answer = 0
    for a in s1:
        for b in s2:
            if a == b: answer += 1
    return answer
#
def solution(s1, s2):
    return len(set(s1)&set(s2));
```