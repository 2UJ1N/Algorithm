import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    s, t = input().split()

    for idx, s in enumerate(s):
        if s == 'X' or s == 'x':
            answer.append(t[idx].upper())
            break

print(''.join(answer))