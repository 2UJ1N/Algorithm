#
# 18258
# 큐 2
# https://www.acmicpc.net/problem/18258

from collections import deque

n = int(input())
queue = deque()

for _ in range(n):
    command = input().split()

    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue: 
            print(queue.popleft())
        else: print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif command[0] == 'front':
        if queue: print(queue[0]) 
        else: print(-1)
    elif command[0] == 'back':
        if queue: print(queue[-1]) 
        else: print(-1)