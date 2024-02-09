#
# 11866
# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
queue = deque(i for i in range(1, n + 1))
answer = []

for _ in range(n):
    for _ in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end="")
for j in range(len(answer) - 1):
    print(answer[j], end=", ")
print(answer[-1], end=">")