#
# 2587
# 대표값2
# https://www.acmicpc.net/problem/2587

number = []
for _ in range(5):
    number.append(int(input()))

print(sum(number) // 5)
print(number[2])