#
# <이것이 코딩테스트다>
# Part6 실전 문제
# 두 배열의 원소 교체

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

# total = arrA + arrB
# total.sort(reverse=True)
# answer = total[:len(arrA)]
# print(answer)

arrA.sort()
arrB.sort(reverse=True)

for i in range(k):
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break

print(sum(arrA))