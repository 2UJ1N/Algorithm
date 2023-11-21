#
# 10952
# A+B - 5
# https://www.acmicpc.net/problem/10952

while 1:
    a, b = map(int, input().split())

    if a == b == 0:
        exit()

    print(a + b)