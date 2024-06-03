def solution(money):
    # 마지막 집을 안 터는 경우
    case1 = [0 for _ in range(len(money))]
    case1[0] = money[0]
    case1[1] = max(money[0], money[1])

    # 첫번째 집을 안 터는 경우
    case2 = [0 for _ in range(len(money))]
    case2[1], case2[2] = money[0], money[1]

    for i in range(2, len(money) - 1):
        case1[i] = max(case1[i - 1], money[i] + case1[i - 2])
    for i in range(2, len(money)):    
        case2[i] = max(case2[i - 1], money[i] + case2[i - 2])
    

    print(case1, case2)
    return print(max(max(case1), max(case2)))

# money = [1, 2, 3, 1]
money = [1, 100, 1, 100, 1]
solution(money)