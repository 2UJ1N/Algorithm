#
# [Level 1] 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0: answer.append(a)
        
        if answer[-1] == a: pass
        else: answer.append(a)
    return answer