#
# 11660
# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for _ in range(n):
    x = list(map(int, input().split()))
    num.append(x)

sumArr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sumArr[i][j] = num[i - 1][j - 1] + sumArr[i - 1][j] + sumArr[i][j - 1] - sumArr[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumArr[x2 + 1][y2 + 1] - sumArr[x1][y2 + 1] - sumArr[x2 + 1][y1] + sumArr[x1][y1])