#
# [Level 1] 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    ponketmon = set(nums)
    
    if len(ponketmon) >= len(nums) // 2: 
        return len(nums) // 2
    else: return len(ponketmon)