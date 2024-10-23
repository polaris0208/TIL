# 배열 자르기
```py
def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer
#
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
```
# 외계 행성 나이
```py
def solution(age):
    str_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    int_ = list(range(0, 10))
    age_dict = dict(zip(int_, str_))
    age_list = list(map(int, str(age)))
    p_age = []
    for _ in age_list:
      p_age.append(age_dict[_])
    answer = ''.join(p_age)
    return answer
#
def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age
```
# 진료 순서
```py
def solution(emergency):
    sorted_e = sorted(emergency, reverse=True)
    answer = []
    for _ in emergency:
        answer.append(sorted_e.index(_) + 1)
    return answer
#
def solution(emergency):
    e = sorted(emergency,reverse=True)
    return [e.index(i)+1 for i in emergency]
```
# 순서쌍
```py
def solution(n):
    answer = 0
    for _ in range(1,n+1):
        if n % _ == 0:
            answer += 1
    return answer
#
def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2

            if i * i == n:
                answer -= 1

    return answer
```