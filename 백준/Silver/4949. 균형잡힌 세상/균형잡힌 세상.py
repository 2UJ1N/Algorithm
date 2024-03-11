#
# 4949
# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

while 1:
    sentence = input()
    stack = []

    if sentence == ".": exit()

    for s in sentence:
        if s == '(' or s == '[': stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(0)
                break
        elif s == ']':
            if stack and stack[-1] == '[': 
                stack.pop()
            else: 
                stack.append(0)
                break
    if stack: 
        print("no")
    else: 
        print("yes")