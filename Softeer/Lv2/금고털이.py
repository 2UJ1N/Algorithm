import sys
input = sys.stdin.readline

w, n = map(int, input().split())
metal = []

for _ in range(n):
    m, p = map(int, input().split())
    metal.append([m, p])

metal.sort(key=lambda x: -x[1])

price = 0
for m, p in metal:
    if w - m >= 0:
        w -= m
        price += m * p
    else:
        price += w * p
        break

print(price)