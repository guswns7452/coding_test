# DFS [안전영역]
# https://www.acmicpc.net/problem/2468

# ⏰ 소요시간 : 35분

import sys, copy
from collections import deque

N = int(sys.stdin.readline())
graph = []

def find_first(graph):
    for idx, i in enumerate(graph):
        for idx_j, j in enumerate(i):
            if j > 0:
                return [idx, idx_j]

def dfs(graph):
    temp_graph = copy.deepcopy(graph)
    stack = deque()    
    four_direction = [-1, 0], [1, 0], [0, -1], [0, 1]
    
    find_list = find_first(temp_graph)
    if find_list == None:
        return 0
    
    area = 0
    while(True):
        while(stack):
            x, y = stack.pop()
            if temp_graph[x][y] > 0:
                temp_graph[x][y] = 0
                for temp_x, temp_y in four_direction:
                    if 0 <= x + temp_x < len(temp_graph) and 0 <= y + temp_y < len(temp_graph[0]) and temp_graph[x + temp_x][y + temp_y] > 0:
                        stack.append([x + temp_x, y + temp_y])
        
        find_list = find_first(temp_graph)
        if find_list == None:
            return area
        else:
            area += 1
            stack.append(find_list)

min_value = 101
max_value = -1               

for i in range(N):
    one_line = list(map(int, sys.stdin.readline().split()))
    graph.append(one_line)
    min_value = min(min_value, min(one_line))
    max_value = max(max_value, max(one_line))    

# 하나씩 잠기게 하여 DFS를 탐색하여 영역 구하기
area = 0
for i in range(1, max_value+1):
    for idx, j in enumerate(graph):
        for idx_k, k in enumerate(j):
            if k <= i:
                graph[idx][idx_k] = 0
    
    num = dfs(graph)
    area = max(area, num)
        
print(area)