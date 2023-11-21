# 다시!
# 5622
# 다이얼
# https://www.acmicpc.net/problem/5622

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
answer = 0

for w in word:
    for n in number:
        if w in n:
            answer *= 10
            answer += number.index(n) + 2
    
chk = str(answer)
cnt = 0
for c in chk:
    cnt += int(c) + 1

print(cnt)