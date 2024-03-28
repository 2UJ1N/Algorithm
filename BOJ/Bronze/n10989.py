#
# 10989
# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

n = int(input())
num = [0] * 10001

for _ in range(n):
    num[int(input())] += 1

for i in range(1, 10001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)