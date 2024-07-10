#
# 3079
# 입국심사
# https://www.acmicpc.net/problem/3079

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
counter = []
for _ in range(n):
    counter.append(int(input()))

print(counter)
