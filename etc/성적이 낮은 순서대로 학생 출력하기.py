#
# <이것이 코딩테스트다>
# Part6 실전 문제
# 성적이 낮은 순서대로 학생 출력하기

import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    name, score = input().split()
    dict[name] = int(score)

dict = sorted(dict.items(), reverse=True)

for i in dict:
    print(i[0], end=' ')