#
# 2501
# 약수 구하기
# https://www.acmicpc.net/problem/2501

n, k = map(int, input().split())
factor = [1]
for i in range(2, n + 1):
    if n % i == 0: factor.append(i)

if len(factor) < k: print(0)
else: print(factor[k - 1])