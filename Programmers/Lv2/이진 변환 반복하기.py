def solution(s):
    cnt, cnt0 = 0, 0
    
    while s != '1':
        cnt += 1
        cnt1 = s.count("1")
        cnt0 += len(s) - cnt1
        
        tmp = bin(cnt1)[2:]
        s = str(tmp)
    
    return [cnt, cnt0]