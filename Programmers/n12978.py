#
# [Level 2] 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    for start, end, time in road:
        graph[start].append((end, time))
        graph[end].append((start, time))

    print(graph)
    distances = dijkstra(graph, 1)
    answer = [i for i in distances if i <= K]
    
    print(distances)
    return print(len(answer))


# 다익스트라 최적경로 탐색
def dijkstra(graph, start):
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return distances 

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

# N = 6
# road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
# K = 4
solution(N, road, K)