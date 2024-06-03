#
# [Level 2] 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = list()
    for i in s:
        if i == '(': stack.append(i)
        elif i == ')':
            if len(stack) != 0:
                stack.pop()
            else: return False
    
    return len(stack) == 0