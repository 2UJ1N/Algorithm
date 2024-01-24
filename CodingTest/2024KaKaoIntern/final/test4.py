from itertools import combinations

def find_target(cards, target):
    allPair = combinations(cards, 2)

    for pair in allPair:
        if sum(pair) == target:
            cards.remove(pair[0])
            cards.remove(pair[1])
    
    return cards

def calculate_round(cards,  target):
    cardcnt = len(cards) // 3
    myCard = find_target(cards[:cardcnt], target)
    round = 0

    # 사용 가능 코인
    buyableCoin = (target - 1) - len(find_firstpair)

    while buyableCoin > 0:
        myCard



    

    
    return 1

def find_target(cards, target):
    allPair = combinations(cards, 2)
    paircnt = 0


    for pair in allPair:
        if sum(pair) == target:
            cards.remove(pair[0])
            cards.remove(pair[1])
            paircnt += 1
        
    return paircnt

def solution(coin, cards):
    target = coin + 1
    idx = len(cards) // 3
    myCard = cards[: idx]
    roundcnt = 0
    paircnt = 0

    firstCase = find_target(myCard, target)

    buyableCoin = coin - firstCase

    while myCard:
        roundcnt += 1

        myCard += cards[idx: idx + 2]
        idx += 2

        if buyableCoin > 0:
            paircnt += find_target(myCard, target)
            buyableCoin -= 1
        else:
            myCard = myCard[2:]
            

    return round + 1

coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
solution(coin, cards)