#
# [Level 2] K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for start, end, num in commands:
        target = array[start - 1 : end]
        answer.append(list(sorted(target))[num -1])

    return answer