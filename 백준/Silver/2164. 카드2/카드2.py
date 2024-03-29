#
# 2164
# 카드 2
# https://www.acmicpc.net/problem/2164

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque(i for i in range(1, n + 1))

for _ in range(n - 1):
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)