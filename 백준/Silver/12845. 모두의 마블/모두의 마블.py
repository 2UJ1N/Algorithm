#
# 12845
# 모두의 마블
# https://www.acmicpc.net/problem/12845

import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort(reverse=True)

gold = sum(card[1:]) + card[0] * (len(card) - 1)
print(gold)