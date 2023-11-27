#
# 24265
# 알고리즘 수업 - 알고리즘의 수행 시간 4
# https://www.acmicpc.net/problem/24265

import sys
input = sys.stdin.readline

n = int(input())

print(int(n * (n - 1) * (n - 2) / 6))
print(3)