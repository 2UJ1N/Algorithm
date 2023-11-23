#
# 2566
# 최댓값
# https://www.acmicpc.net/problem/2566

board = []
max_num = []
loca = []

for i in range(9):
    k = list(map(int, input().split()))
    board.append(k)
    max_num.append(max(k))
    l = [i + 1, k.index(max(k)) + 1]
    loca.append(l)

print(max(max_num))
print(*loca[max_num.index(max(max_num))])