# 다시
# 1157
# 단어 공부
# https://www.acmicpc.net/problem/1157

word = input().upper()

cnt = [0] * 26

for w in word:
    for i in range(ord('A'), ord('Z') + 1):
        if w == chr(i): cnt[ord(w) - ord('A')] += 1

if cnt.count(max(cnt))  == 1: print(chr(cnt.index(max(cnt)) + ord('A')))
else: print("?")