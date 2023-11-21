#
# 3052
# 나머지
# https://www.acmicpc.net/problem/3052

remain = list()
for _ in range(10):
    x = int(input()) % 42
    if x not in remain: remain.append(x)
print(len(remain))