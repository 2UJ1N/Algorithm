#
# [Level 2] 광물 캐기
# https://school.programmers.co.kr/learn/courses/30/lessons/172927

from itertools import permutations

def cntTired(case1, case2):
    tired = 0
    for i in 


def solution(picks, minerals):
    tools = []
    for i in picks:
        if i != 0:
            for _ in range(i):
                tools.append(picks.index(i))
    
    if len(minerals) % 5 == 0:
        cntTool = len(minerals) // 5
    else:
        cntTool = len(minerals) // 5 + 1

    toolCase = list(permutations(tools[:cntTool], cntTool))
    mineralCase = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]

    minTired = 0
    for i in range(len(cntTool)):
        tired = cntTired(toolCase[i], mineralCase[i])
        if minTired == 0: minTired = tired
        if tired < minTired: minTired = tired
    
    print(minTired)


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# 12
# picks = [0, 1, 1]
# minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
# # 50

solution(picks, minerals)