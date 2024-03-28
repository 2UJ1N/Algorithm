#
# 1181
# 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input())
word = [0] * 51

for _ in range(n):
    w = input()
    if word[len(w)] != 0: word[len(w)].append(w)
    else: word[len(w)] = [w]

for w in word:
    if w != 0:
        w.sort()
        for i in w:
            print(i)