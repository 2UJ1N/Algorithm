#
# 1545
# 거꾸로 출력해 보아요
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV2gbY0qAAQBBAS0&categoryId=AV2gbY0qAAQBBAS0&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=20&pageIndex=1

n = int(input())
num = [i for i in range(n + 1)]
print(*num[::-1])