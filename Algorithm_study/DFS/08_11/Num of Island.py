# DFS [섬의 개수]
# https://www.acmicpc.net/problem/4963

# ⏰ 소요시간 : 35분

import sys
from collections import deque

def find_first(graph):
    for idx, i in enumerate(graph):
        for idx_j, j in enumerate(i):
            if j == 1:
                return [idx, idx_j]

def dfs(graph):
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    total = 0
    need_nodes = deque()
    find_list = find_first(graph)
    if find_list != None:
        need_nodes.append(find_list)
        graph[find_list[0]][find_list[1]] = 0
        total += 1
    eight_direction = [[-1,-1], [-1,0], [-1,1], [0, -1], [0, 1], [1,-1], [1,0], [1,1]]
    
    
    while(need_nodes):
        x, y = need_nodes.pop()
        if visited[x][y] == False:
            visited[x][y] = True
            for x_i, y_i in eight_direction:
                if 0 <= x + x_i < len(graph) and 0 <= y + y_i < len(graph[0]) and visited[x + x_i][y + y_i] == False and graph[x + x_i][y + y_i] == 1:
                    graph[x + x_i][y + y_i] = 0
                    need_nodes.append([x+x_i, y+y_i])
                    
        
        if len(need_nodes) == 0:
            find_list = find_first(graph)
            if find_list == None:
                return total
            else:
                need_nodes.append(find_list)
                graph[find_list[0]][find_list[1]] = 0
                total += 1
    
    return total

x, y = map(int, sys.stdin.readline().split())

while(x and y):
    graph = list()
    for _ in range(y):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    print(dfs(graph))
    
    x, y = map(int, sys.stdin.readline().split())