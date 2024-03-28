#
# 2581
# 소수
# https://www.acmicpc.net/problem/2581

def is_prime(x):
    if x == 1: return False
    for i in range(2, x):
        if x % i == 0: return False
    return True

m = int(input())
n = int(input())

find = []
for i in range(m, n + 1):
    if is_prime(i): find.append(i)

if len(find) == 0: print(-1)
else: 
    print(sum(find))
    print(min(find))