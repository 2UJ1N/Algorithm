def solution(numbers):
    num = [i for i in range(10)]
    return sum(list(set(num) - set(numbers)))