#
# 2292
# 벌집
# https://www.acmicpc.net/problem/2292

n = int(input())
cnt = 0
num = 1

while n > num:
    num += 6 * (cnt + 1)
    cnt += 1
print(cnt + 1)