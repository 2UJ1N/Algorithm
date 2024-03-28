#
# 1436
# 영화감독 숌
# https://www.acmicpc.net/problem/1436

n = int(input())

if n == 1: 
    print(666)
    exit()
else: n -= 1

for i in range(1666, 100000000000000):
    if '666' in str(i):
        if n == 1: 
            print(str(i))
            exit()
        else:
            n -= 1