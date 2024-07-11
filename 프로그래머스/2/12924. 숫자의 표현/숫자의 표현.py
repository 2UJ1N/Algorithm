def solution(n):
    cnt = 1
    num = [i for i in range(1, n)]
    
    for i in num:
        tmp = i
        for j in range(i + 1, n):
            tmp += j
            if tmp == n:
                cnt += 1
                break
            elif tmp > n:
                break
                
    return cnt