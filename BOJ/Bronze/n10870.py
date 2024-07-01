#
# 10870
# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

import sys
input = sys.stdin.readline

n = int(input())
number = [0, 1]

for i in range(2, n + 1):
    number.append(number[i - 2] + number[i - 1])

print(number[n])