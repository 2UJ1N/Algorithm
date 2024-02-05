#
# 14215
# 세 막대
# https://www.acmicpc.net/problem/14215

import sys
input = sys.stdin.readline

num = sorted(list(map(int, input().split())))

if num[0] + num[1] > num[2]: print(sum(num))
else: print(2 * (num[0] + num[1]) - 1)