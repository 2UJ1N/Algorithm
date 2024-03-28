def fill_diagram(n, tops):
    cnt_1 = tops.count(1)
    dp = [0] * (n + 1)
    total = 2 * n + 1 + cnt_1
    dp[0] = 1
    dp[1] = total - 1

    # 입력 [1, 0]
    case1 = 2
    # 입력 [1, 1]
    case2 = 16
    # 입력 [0, 0]
    case3 = 3



    for i in range(1, n + 1):
        if 


def solution(n, tops):
    return fill_diagram(n, tops)