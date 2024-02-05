#
# 11005
# 진법 변환 2
# https://www.acmicpc.net/problem/11005

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = ""

while n // b != 0:
    num += number[n % b]
    n //= b
num += number[n]

print(num[::-1])