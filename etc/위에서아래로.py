#
# <이것이 코딩테스트다>
# Part6 실전 문제
# 위에서 아래로

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

answer = sorted(arr, reverse=True)

for i in answer:
    print(i, end=' ')