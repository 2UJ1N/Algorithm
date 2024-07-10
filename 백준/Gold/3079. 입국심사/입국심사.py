#
# 3079
# 입국심사
# https://www.acmicpc.net/problem/3079

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
counter = []
for _ in range(n):
    counter.append(int(input()))

# 최소 시간, 최대 시간
start, end = 0, max(counter) * m
answer = end

while (start <= end):
    mid = (start + end) // 2

    # 각 심사대에서 심사 가능한 최대 인원 수
    total = 0
    for i in range(n):
        total += mid // counter[i]
    
    if (total >= m):
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)
