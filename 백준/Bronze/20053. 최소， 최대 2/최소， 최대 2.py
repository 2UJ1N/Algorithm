#
# 20053
# 최소, 최대 2
# https://www.acmicpc.net/problem/20053

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))

    print(min(num), max(num))