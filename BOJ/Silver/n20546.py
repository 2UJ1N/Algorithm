#
# 20546
# 🐜 기적의 매매법 🐜
# https://www.acmicpc.net/problem/20546

import sys
input = sys.stdin.readline

cash = int(input())
junC, sungC = cash, cash
junS, sungS = 0, 0
tmp , cnt = 0, []

stock = list(map(int, input().split()))

for s in stock:
    junS += junC // s
    junC = junC % s

    if s > tmp: 
        cnt.append(1)
    elif s < tmp:
        cnt.append(-1)

    if len(cnt) >= 3 and cnt[-3:] == [1, 1, 1]:
        sungC += sungS * s
        sungS = 0
    elif len(cnt) >= 3 and cnt[-3:] == [-1, -1, -1]:
        sungS += sungC // s
        sungC = sungC % s
    
    tmp = s

jun = junC + stock[-1] * junS
sung = sungC + stock[-1] * sungS

if jun > sung: print("BNP")
elif jun < sung: print("TIMING")
else: print("SAMESAME")