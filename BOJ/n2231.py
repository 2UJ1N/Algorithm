# 다시
# 2231
# 분해학
# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    num = sum((map(int, str(i))))
    num_sum = i + num

    if num_sum == n:
        print(i)
        exit()

print(0)