def solution(nums):
    ponketmon = set(nums)
    
    if len(ponketmon) >= len(nums) // 2: return len(nums) // 2
    else: return len(ponketmon)