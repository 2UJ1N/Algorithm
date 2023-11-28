#
# 2839
# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += int(num // 5)
    print(count)
    break
  
  num -= 3
  count += 1
  
else:
  print(-1)