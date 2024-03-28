#
# 11650
# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

n = int(input())
dot = []

for _ in range(n):
    x, y = map(int, input().split())
    dot.append([x, y])

dot.sort(key = lambda x: (x[0], x[1]))

for d in dot: print(d[0], d[1])