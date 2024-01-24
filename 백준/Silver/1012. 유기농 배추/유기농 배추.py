import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if field[x][y] == 1:
            field[x][y] = 0
            
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x + 1, y)

            return True
        return False

for _ in range(t):
    m, n, k = map(int, input().split())
    
    field = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())

        field[x][y] = 1
    
    cnt = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt += 1
        
    print(cnt)