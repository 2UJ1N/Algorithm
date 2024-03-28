#
# 9086
# 문자열
# https://www.acmicpc.net/problem/9086

# 문자열 리스트에 넣는데 왜 개행문자가 들어가는지? - 그래서 -2 인덱스 사용함

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = list(input())
    print(word[0], end='')
    print(word[-2])