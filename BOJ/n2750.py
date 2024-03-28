#
# 2750
# 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

n = int(input())
num = list()

for _ in range(n):
    num.append(int(input()))

num.sort()

print(*num, end="\n")