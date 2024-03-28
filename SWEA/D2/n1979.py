#
# 1979
# 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PuPq6AaQDFAUq&categoryId=AV5PuPq6AaQDFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 행검사
    
    print("#" + str(i))