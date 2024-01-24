def solution(coin, cards):
    target = len(cards) + 1
    my_cards = []
    round_count = 0
    my_pair_count = 0

    for i in range(len(cards) // 3):
        my_cards.append(cards[i])
    
    # 초기에 target을 만족하는 카드 페어 제거
    while True:
        pair_found = False
        i = 0
        while i < len(my_cards):
            index = my_cards.index(target - my_cards[i]) if target - my_cards[i] in my_cards[i + 1:] else -1
            if index != -1:
                my_cards.pop(index)
                my_cards.pop(i)
                pair_found = True
                my_pair_count += 1
                break
            i += 1

        if not pair_found:
            break

    my_cards = []
    for i in range(len(cards) // 3):
        my_cards.append(cards[i])
    cards = cards[len(cards) // 3:]

    buyable_coin = (coin - (len(my_cards) - my_pair_count * 2)) // 2

    while my_cards:
        round_count += 1

        if coin > 0:
            i = 0
            while i < 2 and cards:
                if target - cards[0] in my_cards:
                    my_cards.append(cards[0])
                    coin -= 1
                elif buyable_coin > 0:
                    my_cards.append(cards[0])
                    coin -= 1
                    buyable_coin -= 1
                elif my_pair_count == 0 and i == 0 and coin > 1 and cards[0] + cards[1] == target:
                    my_cards.extend(cards[:2])
                    coin -= 2
                    cards = cards[2:]
                    break
                cards.pop(0)
                i += 1
        else:
            cards = cards[2:]

        pair_found = False
        i = 0
        while i < len(my_cards):
            index = my_cards.index(target - my_cards[i]) if target - my_cards[i] in my_cards[i + 1:] else -1
            if index != -1:
                my_cards.pop(index)
                my_cards.pop(i)
                pair_found = True
                break
            i += 1

        if not pair_found:
            return round_count

    round_count += 1

    return round_count