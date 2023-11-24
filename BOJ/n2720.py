#
# 2720
# 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720

returnMoney = [25, 10, 5, 1]

for _ in range(int(input())):
    n = int(input())
    chk = []
    for i in returnMoney:
        chk.append(n // i)
        n %= i
    print(*chk)