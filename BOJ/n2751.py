#
# 2751
# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

num = list()
for _ in range(int(input())):
    num.append(int(input()))

num.sort()
print(*num, end='\n')