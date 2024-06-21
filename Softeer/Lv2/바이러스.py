import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

virus = k
for _ in range(n):
    virus *= p
    virus %= 1000000007

print(virus % 1000000007)