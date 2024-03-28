#
# 10250
# ACM 호텔
# https://www.acmicpc.net/problem/10250

for _ in range(int(input())):
    h, w, n = map(int, input().split())

    roomNum = n // h + 1
    roomFloor = n % h

    print(str(roomFloor) + str(roomNum) if w < 10 else str(roomFloor) + str(0) + str(roomNum))