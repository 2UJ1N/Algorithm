#
# 2029
# 몫과 나머지 출력하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QGNvKAtEDFAUq&categoryId=AV5QGNvKAtEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

for i in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print("#" + str(i), a // b, a % b)