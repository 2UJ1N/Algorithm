##############################################
from collections import defaultdict

def calculate_gift(friends, gifts):
    gift_given = defaultdict(lambda: defaultdict(int))
    gift_received = defaultdict(lambda: defaultdict(int))
    gift_given_cnt = defaultdict(int)
    gift_received_cnt = defaultdict(int)

    # 선물 주고 받은 횟수 기록
    for log in gifts:
        giver, receiver = log.split()
        gift_given[giver][receiver] += 1
        gift_received[receiver][giver] += 1
        gift_given_cnt[giver] += 1
        gift_received_cnt[receiver] += 1

    difference = {friend: gift_given_cnt[friend] - gift_received_cnt[friend] for friend in friends}

    next_gift_cnt = {friend: 0 for friend in friends}

    for i, giver in enumerate(friends):
        for j, receiver in enumerate(friends):
            if i != j:
                given_to_receiver = gift_given[giver][receiver]
                given_to_giver = gift_given[receiver][giver]

                if given_to_receiver > given_to_giver:
                    next_gift_cnt[giver] += 1
                elif given_to_receiver == given_to_giver and difference[giver] > difference[receiver]:
                    next_gift_cnt[giver] += 1

    return next_gift_cnt

def solution(friends, gifts):
    next_gift = calculate_gift(friends, gifts)
    max_gifts_cnt = max(next_gift.values())
    return max_gifts_cnt


