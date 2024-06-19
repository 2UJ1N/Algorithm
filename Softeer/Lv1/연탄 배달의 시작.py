import sys
input = sys.stdin.readline

n = int(input())
town = list(map(int, input().split()))
comb = {}

for i in range(len(town) - 1):
    dist = town[i + 1] - town[i]
    if dist in comb: comb[dist] += 1
    else: comb[dist] = 1

sortComb = dict(sorted(comb.items(), key = lambda x:x[0]))

print(list(sortComb.values())[0])