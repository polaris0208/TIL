def solution(n):
    def fac(i):
        m = 1
        for _ in range(1, i+1):
            m *= _
        return m
    answer = []
    for x in range(1, n + 1):
        if fac(x) < n : answer.append(x)
        elif fac(x) > n : break
        print(fac(x))
    return answer
print(solution(10))