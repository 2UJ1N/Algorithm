from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    case = {}
    need = []
    
    for lang in ['cpp', 'java', 'python', '-']:
        for position in ['backend', 'frontend', '-']:
            for work in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    case[lang + ' ' + position + ' ' + work + ' ' + food] = []
    
    for emp in info:
        lan, pos, wo, fo, score = emp.split()
        for l in [lan, '-']:
            for p in [pos, '-']:
                for w in [wo, '-']:
                    for f in [fo, '-']:
                        case[l + ' ' + p + ' ' + w + ' ' + f].append(int(score))
    
    for q in query:
        condition = q.split(" and ")
        food, score = condition[-1].split()
        
        cond = ' '.join(condition[:-1])
        cond += ' ' + food
        need.append([cond, score])
    
    for n, s in need:
        cand = sorted(case[n])

        answer.append(len(cand) - bisect_left(cand, int(s)))
        
    return answer