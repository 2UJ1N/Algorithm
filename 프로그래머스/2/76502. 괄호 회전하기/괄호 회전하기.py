def solution(s):
    cnt = 0
    if len(s) == 1: return 0
    elif len(s) == 2:
        if s == '()' or s == '[]' or s == '{}':
            return 1
    else:
        for i in range(len(s)):
            target = s[i:] + s[:i]
            stack = []
            flag = 1
            for t in target:
                if t == '(' or t == '{' or t == '[':
                    stack.append(t)
                elif t == ')':
                    if len(stack) != 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        flag = 0
                        break
                elif t == '}':
                    if len(stack) != 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        flag = 0
                        break
                elif t == ']':
                    if len(stack) != 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        flag = 0
                        break
            if len(stack) == 0 and flag == 1: cnt += 1
        return cnt
                    