from itertools import combinations

def cnt_possible_case(dice_cnt, dice):
    return list(combinations(dice, 2)

def cnt_score(diceA, diceB):
    max_sum = len(diceA) * 100

    sumA = [0] * (max_sum + 1)
    sumB = [0] * (max_sum + 1) 

    for A in diceA:
    




def solution(dice):
    dice_cnt = len(dice)
    possible_case = cnt_possible_case(dice_cnt, dice)
    
    max_score = -1
    a_idx = -1
    for case in possible_case:
        score = cnt_score(case)
        if score > max_score:
            max_score = score
            a_idx = case[0]    

    answer = []
    for a in a_idx:
        for i in range(len(dice)):
            if dice[i] == a:
                answer.append(i)
    return answer
