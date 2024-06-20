import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
menu = list(map(int, input().split()))
button = list(map(int, input().split()))

tmp = []
flag = 0

for b in range(n):
    if tmp != menu:
        if b < n - m + 1:
            if button[b] == menu[len(tmp)]:
                tmp.append(button[b])
                flag = 1
            else:
                if flag == 1:
                    tmp = []
                    flag = 0
        else:
            if tmp != menu:
                flag = 0

if tmp == menu and flag == 1: print("secret")
else: print("normal")