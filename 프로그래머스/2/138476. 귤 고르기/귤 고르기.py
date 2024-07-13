from collections import Counter

def solution(k, tangerine):
    cntTan = Counter(tangerine)

    cntT = list(cntTan.values())
    recntT = sorted(cntT, reverse = True)

    
    if max(cntT) >= k: return 1
    elif sum(cntT) == k: return len(cntT)
    else:
        tmp = recntT[0]
        for i in range(1, len(recntT)):
            tmp += recntT[i]
            if tmp >= k:
                return i + 1
        
        