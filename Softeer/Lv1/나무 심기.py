import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
fList = list(map(int, input().split()))

if n == 2: print(fList[0] * fList[1])
else:
    tmp = combinations(fList, 2)
    max = None
    for a, b in tmp:
        if max is None or max < a * b: max = a * b
    print(max)