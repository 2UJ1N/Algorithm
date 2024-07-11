#
# 11728
# 배열 합치기
# https://www.acmicpc.net/problem/11728

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

answer = arrA + arrB
answer.sort()

print(*answer)