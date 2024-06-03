def solution(a, b):
    num = [i for i in range(min(a, b), max(a, b) + 1)]
    return sum(num)