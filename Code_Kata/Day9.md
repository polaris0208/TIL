# 개미 군단
```py
def solution(hp):
    a = hp % 5   
    b = a % 3
    a_ = hp // 5
    b_ = a // 3
    if a == 0 : answer = a_  
    elif a > 0: 
      if b == 0: 
          answer = a_ + b_
      elif b > 0 and b < 3:
          answer = a_ + b_ + b 
      else: answer = a + b
    return answer
#
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
```
# 모스 부호
```py
def solution(letter):
    input_ = letter.split()

    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
        }
    t = []
    for key in input_:
      t.append(morse.get(key))
    return ''.join(t)
#
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

def solution(letter):
    return "".join(map(lambda w: morse[w], letter.split()))
```
# 가위 바위 보
```py
def solution(rsp):
    input = list(str(rsp))
    output = []
    for _ in input:
        if _ == '0' : 
            p = '5' 
            output.append(p)
        elif _ == '2' : 
            r = '0'
            output.append(r)
        elif _ == '5' : 
            c = '2'
            output.append(c)
    answer = ''.join(output)
    return answe
#
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
```

# 구슬 나누기
```py
def solution(balls, share):
    def fac(x):
        fac_n = 1
        for _ in range(1, x+1):
            fac_n *= _
        return fac_n
    answer = fac(balls) / (fac(balls - share) * fac(share))
    return answer
#
import math

def solution(balls, share):
    return math.comb(balls, share)
```