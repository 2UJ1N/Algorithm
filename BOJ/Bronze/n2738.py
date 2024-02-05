# 다시 - 런타임에러
# 2738
# 행렬 덧셈
# https://www.acmicpc.net/problem/2738

n, m = map(int, input().split())
a, b = [], []

for i in range(n):
    k = list(map(int, input().split()))
    a.append(k)
for i in range(n):
    k = list(map(int, input().split()))
    b.append(k)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print()
