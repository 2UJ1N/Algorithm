import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefixSum = [0] + num

for i in range(1, n + 1):
    prefixSum[i] += prefixSum[i - 1]

for _ in range(m):
    start, end = map(int, input().split())
    print(prefixSum[end] - prefixSum[start - 1]) 