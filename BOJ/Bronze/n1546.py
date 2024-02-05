#
# 1546
# 평균
# https://www.acmicpc.net/problem/1546

n = int(input())
grade = list(map(int, input().split()))
m = max(grade)
new_grade = [i / m * 100 for i in grade]
print(sum(new_grade) / len(new_grade))