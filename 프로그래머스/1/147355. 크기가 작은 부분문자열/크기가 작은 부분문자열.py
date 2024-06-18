def solution(t, p):
    num = [int(t[i : i + len(p)]) for i in range(len(t) - len(p) + 1)]
    
    answer = [i for i in num if i <= int(p)]
    print(num)
    print(answer)
    return len(answer)