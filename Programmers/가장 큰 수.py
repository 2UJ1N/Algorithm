#
# [Level 2] K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    arr = [str(i) for i in numbers]
    arr.sort(reverse=True)
    
    arr.sort(key=lambda x : ((str(x) * 6)[:6]), reverse=True)
    
    answer = ''.join(arr)
    
    return answer if answer[0] != '0' else '0'