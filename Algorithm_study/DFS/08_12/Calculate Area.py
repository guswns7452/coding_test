# DFS [영역 구하기]
# https://www.acmicpc.net/problem/2583

import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

def find_first(graph):
    for idx, i in enumerate(graph):
        for idx_j, j in enumerate(i):
            if j == 0:
                return [idx, idx_j]

def dfs(graph):
    stack = deque()
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    find_first_spot = find_first(graph)
    if find_first_spot == None:
        print(0)
        sys.exit()
    stack.append(find_first_spot)
    
    four_direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    count_list = []
    while(find_first_spot):
        count = 0
        while(stack):
            x, y = stack.pop()
            if visited[x][y] == False:
                visited[x][y] = True
                graph[x][y] = 2
                count += 1
                
                for four_x, four_y in four_direction:
                    if 0 <= x + four_x < len(graph) and 0 <= y + four_y < len(graph[0]) and graph[x + four_x][y + four_y] == 0 and visited[x + four_x][y + four_y] == False:
                        stack.append([x + four_x, y + four_y])
        
        count_list.append(count)
        find_first_spot = find_first(graph)
        if find_first_spot != None:
            stack.append(find_first_spot)
        else:
            return count_list

    
graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().split())
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            graph[j][i] = 1
            
count_list = dfs(graph)
print(len(count_list))
print(*sorted(count_list))