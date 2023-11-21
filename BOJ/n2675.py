#
# 2675
# 문자열 반복
# https://www.acmicpc.net/problem/2675

for _ in range(int(input())):
    r, s = input().split()
    for i in s:
        print(i * int(r), end="")
    print()