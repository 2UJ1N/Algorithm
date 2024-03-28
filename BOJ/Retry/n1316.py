# 다시
# 1316
# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    chk = []
    idx = 0
    flag = 1
    for w in word:
        if w not in chk:
            chk.append(w)
        else:
            if not word[idx - 1] == w: flag = 0
        idx += 1
    if flag == 1: cnt += 1

print(cnt)