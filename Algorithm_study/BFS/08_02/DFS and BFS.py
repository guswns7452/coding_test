# BFS [DFS와 BFS]
# https://www.acmicpc.net/problem/1260

# ⏰ 소요시간 : 22분


import sys
from collections import deque

def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, start):
    queue = deque()
    visited_order = list()
    visited[start] = True
    queue.append(start)
    visited_order.append(start)
    
    while(queue):
        next = queue.popleft()
        for i in graph[next]:
            if visited[i] == False:
                queue.append(i)
                visited_order.append(i)
                visited[i] = True
    print()
    print(*visited_order)        
    
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)
for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y);  graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
    
dfs(graph, visited_dfs, V)
bfs(graph, visited_bfs, V)