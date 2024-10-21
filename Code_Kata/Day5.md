# 옷가게 할인
```py
def solution(price):
    if price >= 100000 and price < 300000:
        rate = 0.05
    elif price >= 300000 and price < 500000:
        rate = 0.1
    elif price >= 500000:
        rate = 0.2
    else: rate = 0
    answer = int(price - (price*rate))
    return answer
#
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
```
# 아메리카노
```py
def solution(money):
    answer = []
    cup = money // 5500
    answer.append(cup)
    change =  money % 5500
    answer.append(change)
    return answer
# 
def solution(money):

    answer = [money // 5500, money % 5500]
    return answer
```
# 나이 출력
```py
def solution(age):
    return 2022-age+1
# 
def solution(age):
    return 2023-age
```
# 배열 뒤집기
```py
def solution(num_list):
    answer = []
    len_ =len(num_list)+1
    for x in range(1,len_):
        answer.append(num_list[-x])

    return answer
#
def solution(num_list):
    return num_list[::-1]
```