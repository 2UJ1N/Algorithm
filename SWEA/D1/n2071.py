#
# 2071
# 평균값 구하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

t = int(input())
 
for i in range(1, t + 1):
    num = list(map(int, input().split()))
    avg = round(sum(num) / 10)
    print("#" + str(i), avg)