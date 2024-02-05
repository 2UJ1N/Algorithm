#
# 2745
# 진법 변환
# https://www.acmicpc.net/problem/2745

import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num = 0
bn = list(n) # n 한글자씩
bn.reverse()
chk = 1

for i in bn:
    i = number.index(i)
    
    num += i * chk
    chk *= b
    
print(num)