#
# 1933
# 간단한 N의 약수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PhcWaAKIDFAUq&categoryId=AV5PhcWaAKIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

n = int(input())
divisor = [1, n]

for i in range(2, n):
    if n % i == 0: divisor.append(i)

divisor.sort()
print(*divisor, sep=" ")