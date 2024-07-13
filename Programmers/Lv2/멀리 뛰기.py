from itertools import permutations

def solution(n):
    case = []
    for i in range(n // 2 + 1):
        tmp = []
        for cnt2 in range(i):
            tmp.append(2)
        for cnt1 in range(n - i * 2):
            tmp.append(1)
        case.append(tmp)

    answer = 0
    for c in case:
        chk = set(c)
        if len(chk) == 1:
            answer += 1
        else:
            chk2 = set(list(permutations(c)))
            answer += len(chk2)

    return answer