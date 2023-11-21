#
# 10811
# 바구니 뒤집기
# https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i - 1 : j][::-1]
    basket[i - 1 : j] = tmp

print(*basket)