# 126ms

import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
    a = list(map(int, input().split()))
    board.append(a)

cnt1 = []

for x in range(n - 3 + 1):
    for y in range(n - 3 + 1):
         cnt = 0
         for i in range(3):
            for j in range(3):
                if board[x + i][y + j] == 1:
                    cnt += 1

            cnt1.append(cnt)

print(max(cnt1))