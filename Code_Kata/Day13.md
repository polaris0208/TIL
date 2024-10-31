# 컨트롤 제트
```py
def solution(s):
    answer = 0
    s_list = list(s.split(" "))

    for i in range(0, len(s_list)):
        if s_list[i] == "Z":
            answer -= int(s_list[i-1])
        else:
            answer += int(s_list[i])
    return answer
```
# 배열 원소의 길이
```py
def solution(strlist):
    answer = []
    s = strlist
    for _ in s:
        l = tuple(_)
        n = len(l)
        answer.append(n)
    return answer
#
def solution(strlist):
    answer = list(map(len, strlist))
    return answer
```
# 중복된 문자 제거
```py
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
```

# 삼각형의 조건
```py
def solution(sides):
    s = sorted(sides, reverse = True)
    if s[0] < s[1] + s[2]: answer = 1
    elif s[0] >= s[1] + s[2]: answer = 2
    return answer
#
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
```