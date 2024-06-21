import sys
input = sys.stdin.readline

std = []
test = []

n, m = map(int, input().split())
for _ in range(n):
    dot, speed = map(int, input().split())
    case = [speed] * dot
    std += case

for _ in range(m):
    dot, speed = map(int, input().split())
    case = [speed] * dot
    test += case

max = 0
for i in range(100):
    if test[i] > std[i]:
        over = test[i] - std[i]
        if max < over: max = over

print(max)    