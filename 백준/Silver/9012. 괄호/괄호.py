#
# 9012
# 괄호
# https://www.acmicpc.net/problem/9012

import sys

t = int(input())

for _ in range(t):
    ps = input()
    stack = []
    flag = 0
    for p in ps:
        if p == ')':
            if stack: stack.pop()
            else: 
                print("NO")
                flag = 1
                break
        else: stack.append(p)

    if stack: print("NO")
    else:
        if flag == 0: print("YES")