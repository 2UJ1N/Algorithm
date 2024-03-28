#
# 11931
# 수 정렬하기 4
# https://www.acmicpc.net/problem/11931

import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n): num.append(int(input()))
num.sort(reverse=True)

for i in num: print(i)