#
# 9063
# 대지
# https://www.acmicpc.net/problem/9063

dotx = []
doty = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    dotx.append(x)
    doty.append(y)

minx, maxx = min(dotx), max(dotx)
miny, maxy = min(doty), max(doty)

print((maxx - minx) * (maxy - miny))