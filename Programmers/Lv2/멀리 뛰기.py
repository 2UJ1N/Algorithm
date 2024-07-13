from itertools import permutations

def solution(n):
    case = []
    for i in range(n // 2 + 1):
        add2 = [2] * i
        add1 = [1] * (n - i * 2)
        
        tmp = add2 + add1
        case.append(tmp)

    answer = 0
    for c in case:
        chk = set(c)
        if len(chk) == 1:
            answer += 1
        else:
            chk2 = set(list(permutations(c)))
            answer += len(chk2)

    return answer % 1234567