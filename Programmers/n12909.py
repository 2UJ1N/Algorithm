#
# [Level 1] 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import deque

def solution(s):
    queue = deque()
    
    for i in s:
        if i == '(': queue.append(i)
        elif i == ')':
            if len(queue) == 0: return False
            if queue[0] == '(': queue.popleft()
            else: return False
    
    return len(queue) == 0