#
# 10814
# 나이순 정렬
# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

n = int(input())
people = [0] * 201

for _ in range(n):
    age, name = input().split()
    if people[int(age)] != 0: people[int(age)].append(name)
    else: people[int(age)] = [name]

for i in people:
    if i != 0:
        for j in i: print(people.index(i), j)