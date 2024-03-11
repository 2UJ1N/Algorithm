s = input()
words = [s]
for i in range(1, len(s)):
    words.append(s[i:])

words.sort()
print(*words)