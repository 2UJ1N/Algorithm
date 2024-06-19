import sys
input = sys.stdin.readline

a, b, d = map(int, input().split())

before = (a + b) * (d // a) + (d % a)
if d % a == 0: before -= b
after = (a + b) * (d // b) + (d % b)
if d % b == 0: after -= a
    
print(before + after)