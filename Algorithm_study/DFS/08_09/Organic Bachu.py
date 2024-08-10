# DFS [유기농 배추]
# https://www.acmicpc.net/problem/1012

# ⏰ 소요시간 : 26분

import sys
from collections import deque

# 인접 리스트 찾기
def find_list(bachu, graph, x, y):
    four_direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for list_x, list_y in four_direction:
        if 0 <= x + list_x < len(graph) and 0 <= y + list_y < len(graph[1]) and bachu[x + list_x][y + list_y] == 1:
            graph[x + list_x][y + list_y].append([x, y])
            graph[x][y].append([x + list_x, y + list_y])
    
    return graph

# 탐색할 노드 찾기
def find_start_node(bachu):
    for idx, i in enumerate(bachu):
        for idx_j, j in enumerate(i):
            if j == 1:
                return [idx, idx_j]

# DFS
def dfs(graph, bachu, bachu_count):    
    need_visited = deque()
    
    start_node = find_start_node(bachu)
    
    # 시작 노드 설정해주기
    need_visited.append(start_node)
    
    total = 0
    while(bachu_count):
        # 방문이 필요한 리스트가 아직 존재한다면
        while need_visited:
            # 시작 노드를 지정하고
            x, y = need_visited.pop()

            # 만약 방문한 리스트에 없다면
            if bachu[x][y] == 1:
                # 방문 리스트에 노드를 추가
                bachu[x][y] = 0
                bachu_count -= 1
                # 인접 노드들을 방문 예정 리스트에 추가
                need_visited.extend(graph[x][y])
        
        total += 1
        need_visited.append(find_start_node(bachu))
                
    return total

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    
    bachu = [[[0] for _ in range(N)] for _ in range(M)] # 배추 삽입 위치
    graph = [[[] for _ in range(N)] for _ in range(M)] # 인접 리스트
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bachu[x][y] = 1
        graph = find_list(bachu, graph, x, y) 
        
    print(dfs(graph, bachu, K))