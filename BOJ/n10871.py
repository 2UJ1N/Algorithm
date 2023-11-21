#
# 10871
# X보다 작은 수
# https://www.acmicpc.net/problem/10871

import sys
input = sys.stdin.readline

n, x = map(int, input().split())

num = list(map(int, input().split()))

for i in num:
    if i < x:
        print(i, end=' ')