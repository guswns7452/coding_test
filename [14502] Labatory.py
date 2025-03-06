# BFS & 완전 탐색 [연구소]
# https://www.acmicpc.net/problem/14502

# 소요시간 : 57분

from itertools import combinations
import copy

# 빈 곳 최대값 찾기
global max_empty, N, M
max_empty, N, M = 0, 0, 0

# 안전 구역 범위 찾기
def findSafetyArea(graph):
    total = 0
    for i in graph: 
        total += i.count(0)
    
    return total

# BFS로 탐색
def bfs(graph):
    global max_empty
    safetyArea = findSafetyArea(graph)

    # 바이러스 위치 찾기
    virus_list = []
    for idx, i in enumerate(graph):
        for k in list(filter(lambda x: i[x] == 2, range(len(i)))):
            virus_list.append([idx, k])

    # 탐색하면서 안전 구역 범위 줄이기
    # 만약 안전 구역이 현재 max값보다 작으면 바로 종료함        
    while(virus_list and safetyArea > max_empty):
        x, y = virus_list.pop(0)
        if x+1 < N and graph[x+1][y] == 0: 
            graph[x+1][y] = 2
            safetyArea -= 1
            virus_list.append([x+1, y])

        if x-1 >= 0 and graph[x-1][y] == 0: 
            graph[x-1][y] = 2
            safetyArea -= 1
            virus_list.append([x-1, y])

        if y+1 < M and graph[x][y+1] == 0: 
            graph[x][y+1] = 2
            safetyArea -= 1
            virus_list.append([x, y+1])

        if y-1 >= 0 and graph[x][y-1] == 0: 
            graph[x][y-1] = 2
            safetyArea -= 1
            virus_list.append([x, y-1])

        
    max_empty = max(max_empty, safetyArea)
    
# 입력받기
N, M = map(int, input().split())
input_graph = []
empty_spot = []
for i in range(N):
    oneList = list(map(int, input().split()))
    input_graph.append(oneList)
    for idx, j in enumerate(oneList):
        if j == 0:
            empty_spot.append([i, idx])

# 조합으로 모든 경우의 수 찾기
# 벽 삽입 후 BFS 모든 경우의 수
for i in list(combinations(empty_spot,3)):
    temp_graph = copy.deepcopy(input_graph)
    for j in i:
        temp_graph[j[0]][j[1]] = 1

    bfs(temp_graph)

print(max_empty)

