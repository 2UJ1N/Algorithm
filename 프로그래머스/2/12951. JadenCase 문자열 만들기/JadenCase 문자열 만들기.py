def solution(s):
    word = ''
    answer = ''
    for chk in s:
        if chk != ' ':
            word += chk
        else:
            tmp = word.capitalize()
            answer += tmp
            word = ''
            answer += chk
    tmp = word.capitalize()
    answer += tmp
    
    return answer
            
            