#
# 1085
# 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085

import sys
input = sys.stdin.readline


x, y, w, h = map(int, input().split())

lenX = min(x, w - x)
lenY = min(y, h - y)

print(min(lenX, lenY))