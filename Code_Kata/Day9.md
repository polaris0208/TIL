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