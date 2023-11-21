#
# 2908
# 상수
# https://www.acmicpc.net/problem/2908

a, b = input().split()
num_a = int(a[::-1])
num_b = int(b[::-1])

print(max(num_a, num_b))