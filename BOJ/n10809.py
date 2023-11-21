#
# 10809
# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

s = input()

for i in range(ord('a'), ord('z') + 1):
    print(s.find(chr(i)), end=" ")