def solution(left, right):
    num = [i if cntFactor(i) % 2 == 0 else -i for i in range(left, right + 1)]
    return sum(num)

def cntFactor(num):
    cnt = 0
    if num == 1: return 1
    for i in range(2, num):
        if num % i == 0: cnt += 1
        
    return cnt + 2