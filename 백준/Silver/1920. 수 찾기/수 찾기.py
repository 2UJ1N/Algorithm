#
# 1920
# 수 찾기
# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

for t in target:
    if t in A: print(1)
    else: print(0)