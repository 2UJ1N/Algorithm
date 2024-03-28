#
# 25305
# 커트라인
# https://www.acmicpc.net/problem/25305

n, k = map(int, input().split())
grade = list(map(int, input().split()))
grade.sort()

print(grade[n - k])
