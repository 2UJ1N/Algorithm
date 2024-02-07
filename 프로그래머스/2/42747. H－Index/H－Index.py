def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i + 1 > citations[i] : return citations[i - 1]
    
    return 0