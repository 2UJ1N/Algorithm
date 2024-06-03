#
# [Level 3] 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def findFirstScore(findPlayer, wincnt):
    score = [0 for _ in range(n)]
    for i in findPlayer:
        lose = len(wincnt[i])
        score[lose] = i
    return score

def findNextScore(findPlayer, score, losecnt):
    for p in findPlayer:


# 플루이드마샬

def solution(n, results):
    gamecnt = [0 for _ in range(n + 1)]
    losecnt = [[] for _ in range(n + 1)] # 싸워서 이겼던 사람 목록
    wincnt = [[] for _ in range(n + 1)] # 싸워서 졌던 사람 목록

    for w, l in results:
        losecnt[w].append(l)
        wincnt[l].append(w)
        gamecnt[w] += 1
        gamecnt[l] += 1

    findPlayer = []
    for p in range(n):
        if gamecnt[p] == n - 1:
            findPlayer.append(p)

    # 초기 순위 세팅
    score = findFirstScore(findPlayer, wincnt)
    score = findNextScore(findPlayer, score, losecnt)

    result = 0
    for s in score:
        if s != 0: result += 1
    
    return print(result)

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

solution(n, results)