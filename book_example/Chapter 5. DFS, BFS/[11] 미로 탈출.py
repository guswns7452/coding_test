## Chapter.5 DFS/BFS
## 예제 5-4 미로 탈출

from collections import deque

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph = list(map(int, input().split()))

## 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
    return graph[n-1][m-1]

print(bfs(0,0))
