#
# 1978
# 소수 찾기
# https://www.acmicpc.net/problem/1978

n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in num:
    flag = 0
    if i == 1: flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        cnt += 1
print(cnt)