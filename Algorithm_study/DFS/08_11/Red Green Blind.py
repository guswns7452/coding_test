# DFS [적록 색약]
# https://www.acmicpc.net/problem/10026

# ⏰ 소요시간 : 28분

import sys
from collections import deque

N = int(sys.stdin.readline())

def find_first(visited):
    for idx, i in enumerate(visited):
        for idx_j, j in enumerate(i):
            if visited[idx][idx_j] == False:
                return [idx, idx_j]
        
def dfs(graph):
    visited = [[False for _ in range(len(graph[0]))] for _  in range(len(graph))] 
    stack = deque([[0, 0, graph[0][0]]])
    four_direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    total = 0
    while(True):
        while(stack):
            x, y, char = stack.pop()
            if visited[x][y] == False:
                visited[x][y] = True
                for four_x, four_y in four_direction:
                    if 0 <= x + four_x < len(graph) and 0 <= y + four_y < len(graph[0]) and graph[x + four_x][y + four_y] == char and visited[x + four_x][y + four_y] == False:
                        stack.append([x + four_x, y + four_y, char])
        
        find_list = find_first(visited)
        total += 1
        if find_list == None:
            return total
        else:
            find_list.append(graph[find_list[0]][find_list[1]])
            stack.append(find_list)
            
graph = []
for _ in range(N):
    graph.append(list(*sys.stdin.readline().split()))
    
print(dfs(graph), end=" ")
    
for idx, i in enumerate(graph):
    for idx_j , j in enumerate(i):
        if j == 'G':
            graph[idx][idx_j] = 'R'
                
print(dfs(graph))