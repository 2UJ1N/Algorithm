import sys
input = sys.stdin.readline

n = int(input())
cnt = []

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x, y):
    # 주어진 범위를 벗어나면
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 장애물 개수 체크
        cnt.append(1)
        # 해당 노드 방문 처리
        graph[x][y] = 0

        for a, b in d:
            dfs(x + a, y + b)
        
        return True
    return False

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

result = 0
chkResult = []
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            # 길이로 장애물 개수 확인
            chkResult.append(len(cnt))
            cnt = []

print(result)
chkResult.sort()
for r in chkResult:
    print(r)