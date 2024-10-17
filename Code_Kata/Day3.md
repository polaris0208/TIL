# 두 수의 나머지 
```py
def solution(num1, num2):
    num1 %= num2
    answer = num1
    return answer
#
def solution(num1, num2):
    #return num1%num2
    while num1 >= num2:
        num1 -= num2
    return num1
```

# 중앙값
```py
import numpy as np

def solution(array):
    arr = np.array(array)
    arr = np.sort(arr)
    answer = np.median(arr)
    return answer
#
def solution(array):
    array = sorted(array)
    length = len(array)//2
    return array[length]
```
# 최빈값...
```py
def solution(array):
    set_array = set(array)
    max_count = 0
    for i in set_array:
        count = array.count(i)
        if max_count < count:
            max_count = count
            answer = i
        elif max_count == count:
            answer = -1
    return answer
#
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]
```


# 홀수 구하기
```py
def solution(n):
    nums = list(range(1, n+1))
    answer = []
    for num in nums:
        if num%2 == 0: continue
        else: answer.append(num)

    return answer
#
def solution(n):
    return [x for x in range(n + 1) if x % 2]
```