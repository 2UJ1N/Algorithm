#
# 14467
# 소가 길을 건너간 이유 1
# https://www.acmicpc.net/problem/14467

import sys
input = sys.stdin.readline

n = int(input())
dict = {}
cnt = 0

for _ in range(n):
    cow, position = map(int, input().split())

    if cow not in dict:
        dict[cow] = position
    else:
        if dict[cow] != position:
            cnt += 1
            dict[cow] = position

print(cnt)