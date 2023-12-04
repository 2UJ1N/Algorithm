#
# 1936
# 1대1 가위바위보
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

case = list(map(int, input().split()))

Awin = [[1, 3], [2, 1], [3, 2]]
Bwin = [[1, 2], [2, 3], [3, 1]]

print("A") if case in Awin else print("B")