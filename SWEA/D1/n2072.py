#
# 2072
# 홀수만 더하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

t = int(input())
 
for test_case in range(1, t + 1):
    num = map(int, input().split())
    sum = 0
    for i in num:
        if i % 2 != 0: sum += i
    print("#" + str(test_case), sum)