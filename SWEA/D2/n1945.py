#
# 1945
# 간단한 소인수분해
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

number = [2, 3, 5, 7, 11]
t = int(input())

for i in range(1, t + 1):
    answer = [0, 0, 0, 0, 0]
    n = int(input())

    for j in range(5):
        while n % number[j] == 0:
            answer[j] += 1
            n //= number[j]

    print("#" + str(i), *answer)