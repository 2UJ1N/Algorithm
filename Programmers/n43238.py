import heapq

def solution(n, times):
    test = len(times)
    n -= test
    heapq.heapify(times)
    answer = 0


    return answer

n = 6
times = [7, 10]
solution(n, times)