import sys

for _ in range(int(input())):
    num = int(input())
    while num // 5 != 0:
        print("++++ " * (num // 5), end='')
        num %= 5
    print("|" * num)