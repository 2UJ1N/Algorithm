#
# 1212
# 8진수 2진수
# https://www.acmicpc.net/problem/1212

import sys
input = sys.stdin.readline

n = input()
origin = int(n, 8)
print(bin(origin)[2:])