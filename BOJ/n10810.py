#
# 10810
# 공 넣기
# https://www.acmicpc.net/problem/10810

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    start, end, num = map(int, input().split())
    for i in range(start - 1, end):
        basket[i] = num
print(*basket)