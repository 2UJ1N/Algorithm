import itertools 

def solution(number):
    cnt = 0
    case = list(itertools.combinations(number, 3))
    for c in case:
        if sum(c) == 0: cnt += 1
    return cnt