def solution(s):
    word = list(s.lower().split(' '))
    answer = []
    for w in word:
        case = [w[i].upper() if i % 2 == 0 else w[i] for i in range(len(w))] 
        answer.append(''.join(case))

    return ' '.join(answer)