#
# 15688
# 수 정렬하기 5
# https://www.acmicpc.net/problem/15688

import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)