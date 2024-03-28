from collections import defaultdict

def next_month(friends, gifts):
    gift_given = defaultdict(lambda: defaultdict(int))
    gift_received = defaultdict(lambda: defaultdict(int))
    gift_given_cnt = defaultdict(int)
    gift_received_cnt = defaultdict(int)

    for log in gifts:
        giver, receiver = log.split()
        # 선물 기록 확인용
        gift_given[giver][receiver] += 1
        gift_received[receiver][giver] += 1
        # 선물 지수 확인용
        gift_given_cnt[giver] += 1
        gift_received_cnt[receiver] += 1

        # 선물 지수
        gift_point = {friend: gift_given_cnt[friend] - gift_received_cnt[friend] for friend in friends}

        next_month_gift = {friend: 0 for friend in friends}
        for i, giver in enumerate(friends):
            for j, receiver in enumerate(friends):
                if i != j:
                    gift_g_to_r = gift_given[giver][receiver]
                    gift_r_to_g = gift_given[receiver][giver]

                    if gift_g_to_r > gift_r_to_g:
                        next_month_gift[giver] += 1
                    elif gift_g_to_r == gift_r_to_g and gift_point[giver] > gift_point[receiver]:
                        next_month_gift[giver] += 1

    return next_month_gift.values()

def solution(friends, gifts):
    gift_cnt = next_month(friends, gifts)
    max_gifts = max(gift_cnt)
    return max_gifts

friends = ['joy', 'brad', 'alessandro', 'conan', 'david']
gifts = ['alessandro brad', 'alessandro joy', 'alessandro conan', 'david alessandro', 'alessandro david']

print(solution(friends, gifts))