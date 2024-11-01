# 가까운 수 
```py
def solution(array, n):
    box = []
    array.sort()
    for i in array:
        box.append(abs(n-i))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
#
def solution(array, n):
    array.sort()
    temp = []

    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]
```
# 369
```py
def solution(order):
    l = list(str(order))
    a = l.count('3')
    b = l.count('6')
    c = l.count('9')
    answer = a+b+c
    return answer
#
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
```
# 암호해독
```py
def solution(cipher, code):
    c = list(cipher)
    l = len(c)
    key = l // code
    answer = []
    for _ in range(1, key+1):
        v = c[code*_-1]
        answer.append(v)
    return ''.join(answer)
#
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
```
# 대소문자
```py
def solution(my_string):
    l = list(my_string)
    answer = []
    for _ in l:
        if _.islower() == True: 
            a = _.upper()
            answer.append(a)
        else: 
            a = _.lower()
            answer.append(a)

    return ''.join(answer)
#
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
```