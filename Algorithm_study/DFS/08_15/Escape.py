# BFS [탈출]
# https://www.acmicpc.net/problem/2644

# ⏰ 소요시간 : 60분

import sys, copy
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = []
start_point = []
end_point = []
graph_history = dict()

for i in range(R):
    one_line = list(*sys.stdin.readline().split())
    graph.append(one_line)
    if not start_point and 'S' in one_line:
        start_point = [i, one_line.index('S')]
    
    if not end_point and 'D' in one_line:
        end_point = [i, one_line.index('D')]

# 1초마다 물이 불어나는 것을 기록해둠. 
# graph_history Dictionary에 기록해두어 빠르게 접근 가능.
def oneSecondFlow(graph, time):
    global graph_history
    four_dirction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    try:
        return graph_history[time]
    
    except KeyError:
        if time == 1:
            temp_graph = copy.deepcopy(graph)
            for idx, i in enumerate(graph):
                for idx_j, j in enumerate(i):
                    if j == '*':
                        for x, y in four_dirction:
                            if 0 <= idx + x < len(temp_graph) and 0 <= idx_j + y < len(temp_graph[0]) and graph[idx + x][idx_j + y] == '.':
                                temp_graph[idx + x][idx_j + y] = '*'
            graph_history[time] = temp_graph
    
        else:
            temp_graph = copy.deepcopy(graph_history[time-1])
            for idx, i in enumerate(graph_history[time-1]):
                for idx_j, j in enumerate(i):
                    if j == '*':
                        for x, y in four_dirction:
                            if 0 <= idx + x < len(graph) and 0 <= idx_j + y < len(graph[0]) and graph_history[time-1][idx + x][idx_j + y] == '.':
                                temp_graph[idx + x][idx_j + y] = '*'
            graph_history[time] = temp_graph
            
        return graph_history[time]
            
def bfs(graph):
    global start_point, end_point
    queue = deque([[start_point[0], start_point[1], 0]])
    visited = [[[False, -1] for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[start_point[0]][start_point[1]] = [True, 0]
    
    four_dirction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while(queue):
        x, y, time = queue.popleft()
        graph = oneSecondFlow(graph, time+1)
                
        for temp_x, temp_y in four_dirction:
            sum_x = x + temp_x;  sum_y = y + temp_y;
            if 0 <= sum_x < len(graph) and 0 <= sum_y < len(graph[0]) and (graph[sum_x][sum_y] == '.' or graph[sum_x][sum_y] == 'D') and not visited[sum_x][sum_y][0]:
                queue.append([sum_x, sum_y, time+1])
                visited[sum_x][sum_y] = [True, time+1]    
    
    # Queue를 다 탐색했는데도 방문을 못했다는 것은 접근 불가
    if not visited[end_point[0]][end_point[1]][0]:
        return "KAKTUS"
    
    # 시간 구할 수 있음
    else:
        return visited[end_point[0]][end_point[1]][1]
    
print(bfs(graph))