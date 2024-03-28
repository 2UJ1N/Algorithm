#
# 15552
# 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)