#
# 2798
# 블랙잭
# https://www.acmicpc.net/problem/2798

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort(reverse=True)
card = list(combinations(number, 3))
find = list()

for i in card:
    if sum(i) <= m:
        find.append(sum(i))

print(max(find))