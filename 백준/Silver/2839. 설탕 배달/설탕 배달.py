# <다이나믹 프로그래밍>
# 2839
# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

n = int(input())

suger = [3, 5]

how = [5001] * (n + 5) # n값이 최대 5000 이므로 ..
how[3] = 1
how[5] = 1

for i in range(6, n + 1):
    how[i] = min(how[i - 3], how[i - 5]) + 1

if how[n] < 5001:   # ==5001 하면 반례 나옴 ... N이 7인 경우... 7-3=4, 7-5=2 --> 2, 4 모두 5001이 기본값이기 때문에 5002가 답으로 반환될 수 있다.
    print(how[n])
else:
    print(-1)