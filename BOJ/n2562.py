#
# 2562
# 최댓값
# https://www.acmicpc.net/problem/2562

num_list = [int(input()) for i in range(9)]
print(max(num_list))
print(num_list.index(max(num_list)) + 1)