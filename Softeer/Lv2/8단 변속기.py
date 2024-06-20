import sys
input = sys.stdin.readline

num = list(map(int, input().rstrip().split()))
a = [i for i in range(1, 9)]
b = sorted(a, reverse=True)

if num == a: print("ascending")
elif num == b: print("descending")
else: print("mixed")