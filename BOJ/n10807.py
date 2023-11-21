#
# 10807
# 개수 세기
# https://www.acmicpc.net/problem/10807

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

print(num.count(int(input())))


