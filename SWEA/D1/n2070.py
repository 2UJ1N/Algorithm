#
# 2070
# 큰 놈, 작은 놈, 같은 놈
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

t = int(input())
 
for i in range(1, t + 1):
    a, b = map(int, input().split())
    if a > b : c = ">"
    else:
        if a == b : c = "="
        else: c = "<"
    print("#" + str(i), c)