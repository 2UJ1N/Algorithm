#
# 2941
# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

chk = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
final = word
cnt = 0

for c in chk:
    word = word.replace(c, "*")
print(len(word))