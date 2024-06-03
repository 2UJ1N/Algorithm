def solution(s):
    word = sorted(list(s), reverse = True)
    return ''.join(word)