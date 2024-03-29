#
# 10825
# 국영수
# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

n = int(input())
grade = []

for _ in range(n):
    name, kor, eng, math = input().split()
    grade.append([name, int(kor), int(eng), int(math)])

grade.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

answer = [g[0] for g in grade]
for student in answer: print(student)
