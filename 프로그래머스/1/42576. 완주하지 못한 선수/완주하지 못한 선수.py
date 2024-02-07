from collections import Counter

def solution(participant, completion):
    
    part = Counter(participant)
    comp = Counter(completion)
    
    return ''.join(part - comp)