#
# 24313
# 알고리즘 수업 - 점근적 표기 1
# https://www.acmicpc.net/problem/24313

import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

n = n0
for _ in range(100):
    if a1 * n + a0 > c * n:
        print(0)
        exit()
    n += 1
print(1)