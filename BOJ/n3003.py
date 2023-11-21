#
# 3003
# 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

ki, qu, lo, bi, ni, fo = map(int, input().split())
print(1 - ki, 1 - qu, 2 - lo, 2 - bi, 2 - ni, 8 - fo)