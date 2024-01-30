# 114ms

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
happyNum = 0

for _ in range(n):
    board.append(list(map(int, input().split())))

def is_happy_sequence(squence):
    cnt, maxCnt = 1, 1
    
    for j in range(len(i) - 1):
        if squence[j] == squence[j + 1]: cnt += 1
        else: cnt = 1

        maxCnt = max(maxCnt, cnt)
    return maxCnt >= m

for i in board:
    if is_happy_sequence(i): happyNum += 1

board2 = list( zip( *board ))
for i in board2:
    if is_happy_sequence(i): happyNum += 1

print(happyNum)