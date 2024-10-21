# 문자열 뒤집기
```py
def solution(my_string):
    letters = list(my_string)
    reverse = []
    len_ =len(letters)+1
    for x in range(1,len_):
      reverse.append(letters[-x])
    answer = ''.join(reverse)
    return answer
#
def solution(my_string):
    return my_string[::-1]
#  sequence[start:stop:step] -1씩 이동
```
# 직각 삼각형 출력하기
```py
n = int(input())
nums = range(1, n+1, 1)
star = ('*')
for num in nums:
    triangler = star * num
    print(triangler)
#
n = int(input())
for i in range(n):
    print('*'*(i+1))
```
# 짝수 홀수
```py
def solution(num_list):
    even = []
    odd = []
    for num in num_list:
        if num % 2 == 0 : 
            even.append(num)
        else: odd.append(num)

    return (len(even), len(odd))
#
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
```
# 문자 반복
```py
def solution(my_string, n):
    letters = list(my_string)
    multi = []
    len_ =len(letters) + 1
    for x in range(1,len_):
      letter = n * letters[x-1]
      multi.append(letter)
    answer = ''.join(multi)
    return answer
#
def solution(my_string, n):
    answer = ''

    for c in list(my_string):
        answer += c*n
    return answer
```