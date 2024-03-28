#
# 1889
# 초심자의 회문 검사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PyTLqAf4DFAUq&categoryId=AV5PyTLqAf4DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=2&pageSize=20&pageIndex=1
 
t = int(input())
for i in range(1, t + 1):
    word = input()
    print("#" + str(i), end=" ")
    print(1 if word == word[::-1] else 0)