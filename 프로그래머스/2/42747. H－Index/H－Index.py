def solution(citations):
    citations.sort(reverse=True)
    
    for i in reversed(range(len(citations) + 1)):
        cnt = 0
        for c in citations:
            if c >= i: cnt += 1
        
        if cnt >= i: return i
    return 0
    #         cnt += 1
    #         if c <= i:
    #             break
    #     if cnt >= i: return i
    # return 0