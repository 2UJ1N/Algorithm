#
# 1959
# 두 개의 숫자열
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))

    answer = []

    if n == m:
        x = 0
        for j in range(n):
            x += nList[j] * mList[j]
        answer.append(x)
    elif n > m:
        for j in range(n - m):
            x = 0
            for k in range(m):
                answer

    else:
        for j in range(m - n):



    print("#" + str(i), max(answer))