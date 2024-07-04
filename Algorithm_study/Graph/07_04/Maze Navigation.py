import sys
from collections import deque

def bfs(n, m, maze):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque([(0, 0)])
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1
    
    while q:
        x, y = q.popleft()
        for d in dir:
            xx, yy = x + d[0], y + d[1]
            if 0 <= xx < n and 0 <= yy < m and maze[xx][yy] == 1 and check[xx][yy] == 0:
                q.append((xx, yy))
                check[xx][yy] = check[x][y] + 1
    
    return check[n-1][m-1]

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    
print(bfs(n, m, maze))


