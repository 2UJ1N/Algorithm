import sys
input = sys.stdin.readline

h, m = 0, 0

for _ in range(5):
    start, end = input().split()
    starth, startm = map(int, start.split(":"))
    endh, endm = map(int, end.split(":"))
    h += endh - starth
    m += endm - startm

print(60 * h + m)