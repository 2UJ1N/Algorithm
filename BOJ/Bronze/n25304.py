#
# 25304
# 영수증
# https://www.acmicpc.net/problem/25304

x = int(input())
n = int(input())

total = 0

for _ in range(n):
    price, num = map(int, input().split())
    total += price * num

print("Yes") if x == total else print("No")