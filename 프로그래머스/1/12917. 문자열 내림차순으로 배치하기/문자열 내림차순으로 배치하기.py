def solution(s):
    word = list(s)
    word.sort(reverse = True)
    return ''.join(word)