# BFS [DFS와 BFS]
# https://www.acmicpc.net/problem/1303

# ⏰ 소요시간 : 40분

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# Visited 이중 리스트 만들기
visited = [[False] * N]* M

# 값 입력 받아, 리스트에 넣기
input_list = []
for _ in range(M):
    input_list.append(list(''.join(sys.stdin.readline().split())))


# 연결 리스트로 변경 (Set)으로 넣기
graph = [[[] for _ in range(N)] for _ in range(M)]

for idx_m, val_m in enumerate(input_list):
    for idx_n, val_n in enumerate(val_m):
        # 아래쪽 판단
        if idx_m + 1 < M and input_list[idx_m + 1][idx_n] == val_n: 
            graph[idx_m][idx_n].append([idx_m+1, idx_n])
            graph[idx_m+1][idx_n].append([idx_m, idx_n])
            
        # 오른쪽 판단    
        if idx_n + 1 < N and input_list[idx_m][idx_n + 1] == val_n:
            graph[idx_m][idx_n].append([idx_m, idx_n+1])
            graph[idx_m][idx_n+1].append([idx_m, idx_n])
        
# 새로운 위치 탐색하기
def find_first(visited):
    for i, v in enumerate(visited):
        if False in v:
            return [i, v.index(False)]

# bfs
def bfs(graph, visited, count):
    queue = deque()
    visited[0][0] = True
    queue.append([0,0])
    temp_count = 0
    total = [0, 0] # W B 의 개수
    
    while(count):
        next = queue.popleft()
        count -= 1
        temp_count += 1 
        for i in graph[next[0]][next[1]]:
            if visited[i[0]][i[1]] == False:
                queue.append(i)
                visited[i[0]][i[1]] = True

        # 더 이상 연결되어 있지 않으면
        if (not queue):
            # 여태까지 값 더해야함
            if input_list[next[0]][next[1]] == 'W':
                total[0] += (temp_count**2)
            else:
                total[1] += (temp_count**2)
            
            temp_count = 0
            
            x = find_first(visited)
            if not count: # 탐색할 것이 없으면
                break
            queue.append(x)
            visited[x[0]][x[1]] = True
    
    print(*total)
visited = [[False for _ in range(N)] for _ in range(M)]

bfs(graph, visited, N*M)