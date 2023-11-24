#
# 9506
# 약수들의 합
# https://www.acmicpc.net/problem/9506

while 1:
    n = int(input())
    if n == -1: exit()

    factor = [1]
    for i in range(2, n):
        if n % i == 0: factor.append(i)

    if sum(factor) == n:
        print(n, "=", end=" ")
        print(*factor, sep=" + ")
    else: print(n, "is NOT perfect.")