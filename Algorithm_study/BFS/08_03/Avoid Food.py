# BFS [음식물 피하기]
# https://www.acmicpc.net/problem/1743

# ⏰ 소요시간 : 30분

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(M)] for _ in range(N)]

# 하나씩 입력 받아서 그래프 그리기
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1

adjacency_list = [[[] for _ in range(M)] for _ in range(N)]

visited = [[[] for _ in range(M)] for _ in range(N)]

# 인접 리스트로 변경
for idx, val in enumerate(graph):
    for idx_j, val_j in enumerate(val):
        if graph[idx][idx_j] == 1:
            visited[idx][idx_j] = False
            # 아래쪽 판단
            if idx + 1 < N and graph[idx + 1][idx_j] == 1: 
                adjacency_list[idx][idx_j].append([idx+1, idx_j])
                adjacency_list[idx+1][idx_j].append([idx, idx_j])
            
            # 오른쪽 판단    
            if idx_j + 1 < M and graph[idx][idx_j + 1] == 1:
                adjacency_list[idx][idx_j].append([idx, idx_j+1])
                adjacency_list[idx][idx_j+1].append([idx, idx_j])
            

def find_first(visited):
    for idx, i in enumerate(visited):
        for idx_j, j in enumerate(i):
            if j == False:
                return [idx, idx_j]
    
    return False

def bfs(graph, visited):
    a = find_first(visited)
    total = 0
    while(a):
        count = 0
        queue = deque()
        queue.append(a)
        visited[a[0]][a[1]] = True
        count += 1
        
        while(queue):
            x = queue.popleft()
            for i in graph[x[0]][x[1]]:
                if not visited[i[0]][i[1]]:
                    queue.append(i)
                    visited[i[0]][i[1]] = True
                    count += 1
        
        total = max(count, total)
        a = find_first(visited)

    return total
        
print(bfs(adjacency_list, visited))