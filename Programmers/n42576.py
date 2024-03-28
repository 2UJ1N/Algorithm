#
# [Level 1] 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    
    part = Counter(participant)
    comp = Counter(completion)
    
    return ''.join(part - comp)