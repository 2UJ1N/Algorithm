# 
# 10798
# 세로읽기
# https://www.acmicpc.net/problem/10798

word = []
lenWord = []

for _ in range(5):
    x = input()
    word.append(x)
    lenWord.append(len(x))

board = [[] for i in range(max(lenWord))]

for i in word:
    for j in range(len(i)):
        board[j].append(i[j])

for i in board:
    print(*i, sep="", end="")