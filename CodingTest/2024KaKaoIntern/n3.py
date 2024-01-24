def solution(dice):
    n = len(dice)
    case = [0] * n
    best_case = []
    max_win = -1

    if n > 2:
        case[n // 2:] = [1] * (n - n // 2)
    elif n == 2:
        case[1] = 1

    while True:
        A, B = [], []
        for i in range(n):
            if case[i] == 0:
                A.append(dice[i])
            else:
                B.append(dice[i])

        score = calculate_score(A, B)

        if max_win < score[0]:
            max_win = score[0]
            best_case = find_index(case)

        if not next_permutation(case):
            break

    return best_case
