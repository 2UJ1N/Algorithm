#
# 2068
# 최대수 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

t = int(input())
 
for i in range(1, t + 1):
    num = map(int, input().split())
    print("#" + str(i), max(num))