#
# 2563
# 색종이
# https://www.acmicpc.net/problem/2563

import sys
input = sys.stdin.readline

board = [[0 for j in range(100)] for i in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

total = 0
for i in board:
    total += sum(i)
print(total)