#
# 28279
# 덱 2
# https://www.acmicpc.net/problem/28279

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    command = input().split()

    if command[0] == "1":
        queue.appendleft(int(command[1]))
    elif command[0] == "2":
        queue.append(int(command[1]))
    elif command[0] == "3":
        if queue: print(queue.popleft())
        else: print(-1)
    elif command[0] == "4":
        if queue: print(queue.pop())
        else: print(-1)
    elif command[0] == "5":
        print(len(queue))
    elif command[0] == "6":
        if queue: print(0)
        else: print(1)
    elif command[0] == "7":
        if queue: print(queue[0])
        else: print(-1)
    elif command[0] == "8":
        if queue: print(queue[-1])
        else: print(-1)