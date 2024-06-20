import sys
input = sys.stdin.readline

t = int(input())

number = {
    0 : '1110111',
    1 : '0010010',
    2 : '1011101',
    3 : '1011011',
    4 : '0111010',
    5 : '1101011',
    6 : '1101111',
    7 : '1110010',
    8 : '1111111',
    9 : '1111011'
}

for _ in range(t):
    a, b = input().split()

    caseA, caseB = [], []
    for i in reversed(a):
        caseA.append(number[int(i)])
    if len(a) != 5:
        for _ in range(5 - len(a)):
            caseA.append('0000000')

    for i in reversed(b):
        caseB.append(number[int(i)])
    if len(b) != 5:
        for _ in range(5 - len(b)):
            caseB.append('0000000')

    answer = 0
    for i in range(5):
        for j in range(7):
            if caseB[i][j] != caseA[i][j]:
                answer += 1

    print(answer)
