#
# 1193
# 분수찾기
# https://www.acmicpc.net/problem/1193

x = int(input())
line = 1
i = 1

while line < x:
    i += 1
    line += i

cnt = int((i - 1) * i / 2)
chk = []
for j in range(1, i + 1):
    demo = str(j) + "/" + str(i - j + 1)
    chk.append(demo)

if i % 2 == 1:
    chk.reverse()

idx = x - cnt
print(chk[idx - 1])
