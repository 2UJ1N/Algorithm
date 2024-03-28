import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(list(map(int, input().split())))
revboard = list(zip(*board))

def chktype1(): # 첫 번째 블럭 확인
    sumtype1 = []
    for i in range(m - 2 + 1):
        for j in range(n - 2 + 1):
            chk = []
            chk.append(board[i][j])
            chk.append(board[i][j + 1])
            chk.append(board[i + 1][j])
            chk.append(board[i + 1][j + 1])
            sumtype1.append(sum(chk) - min(chk))
    return max(sumtype1)

def chktype2(): # 두 번째 블럭 확인
    maxtype2 = 0
    # 가로
    for i in board:
        for j in range(m - 3 + 1):
            find = i[j] + i[j + 1] + i[j + 2]
            if find > maxtype2: maxtype2 = find
    # 세로
    for i in revboard:
        for j in range(n - 3 + 1):
            find = i[j] + i[j + 1] + i[j + 2]
            if find > maxtype2: maxtype2 = find

    return maxtype2

a, b = chktype1(), chktype2()
print(max(a, b))