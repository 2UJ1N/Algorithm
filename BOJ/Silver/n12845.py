#
# 12845
# 모두의 마블
# https://www.acmicpc.net/problem/12845

import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)

gold = 0
level = 0
for i in range(len(card) - 1):
    if card[i] > level: level = card[i]
    if card[i + 1] <= level: gold += level + card[i + 1]

print(gold)