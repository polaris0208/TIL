# 점의 위치 구하기
```py
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0 : answer = 1
        elif dot[1] < 0 : answer = 4
    elif dot[0] < 0:
        if dot[1] > 0 : answer = 2
        elif dot[1] < 0 : answer = 3
    return answer
#
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
```

# 2차원 만들기
```py
import numpy as np
def solution(num_list, n):
    a = len(num_list) // n
    b = np.array(num_list)
    c = b.reshape(a, n)
    answer = c.tolist()
    return answer
# 
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
```
# 공 던지기
```py
def solution(numbers, k):
    answer = 0
    return numbers[2 * (k - 1) % len(numbers)]
```

# 배열 회전시키기
```py
def solution(numbers, direction):
    if direction == 'left':
        l = []
        for _ in range(1, len(numbers)):
            a = numbers[_]
            l.append(a)
        l.append(numbers[0])
        answer = l
    else: 
        l = [numbers[-1]]
        for _ in range(0, len(numbers)-1):
            a = numbers[_]
            l.append(a)
        answer = l

    return answer
#
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
```