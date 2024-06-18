import sys

input = sys.stdin.readline

n = int(input())
std = None
x, y = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    if std is None or b < std: 
        std = b
        x, y = a, b

print(x, y)

# 단순히 x, y = 0, 0으로 선언했기 때문에 입력값이 양수만 있는 경우 오답!