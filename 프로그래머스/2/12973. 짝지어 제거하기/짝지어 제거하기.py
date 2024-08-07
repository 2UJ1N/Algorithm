def solution(s):
    stack = [s[0]]
    for i in s[1:]:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0: return 1
    else: return 0