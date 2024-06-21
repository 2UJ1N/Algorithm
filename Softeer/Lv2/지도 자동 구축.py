import sys
input = sys.stdin.readline

n = int(input())

cnt = 2 ** (n)
print((cnt + 1) ** 2)