#
# 2903
# 중앙 이동 알고리즘
# https://www.acmicpc.net/problem/2903

n = int(input())

box = []
dot = []

for i in range(n):
    box.append(2 ** (i + 1))

for i in box:
    dot.append((i + 1) ** 2)

print(dot[-1])