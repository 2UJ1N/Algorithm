#
# 1181
# 단어 정렬
# https://www.acmicpc.net/problem/1181

n = int(input())
words = [str(input()) for i in range(n)]

word = list(set(words))
word.sort()
word.sort(key=len)

for w in word: print(w)