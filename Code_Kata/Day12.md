# 모음 제거
```py
def solution(my_string):
    list_ = ['a', 'e', 'i', 'o', 'u']
    answer = [letter for letter in my_string if letter not in list_]
    answer = ''.join(answer)
    return answer
#
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
```
# 문자열 정렬 1
```py
def solution(my_string):

    answer = [int(num) for num in my_string if num in list('0123456789')]
    return sorted(answer)
#
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
```
# 숨어있는 숫자의 덧셈
```py
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())
```
# 소인수 분해
```py
def solution(n):
    k = 2
    answer = []
    while n > 1:
        if n%k == 0: 
            answer.append(k)
            while n%k == 0: n //= k
        k += 1 
    return answer
```