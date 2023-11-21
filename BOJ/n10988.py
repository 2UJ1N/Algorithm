#
# 10988
# 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988

word = input()

print(1) if word == word[::-1] else print(0)
# flag = 1

# for i in range(len(word) // 2):
#     if word[i] != word[-1 - i]: flag = 0

# print(1) if flag == 1 else print(0)