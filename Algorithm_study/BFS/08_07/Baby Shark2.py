# BFS [아기 상어 2]
# https://www.acmicpc.net/problem/17086

# ⏰ 소요시간 : 50분

import sys
from collections import deque

# 입력 받기
sea = []
queue = deque()
shark = []

N, M = map(int, sys.stdin.readline().split())
distance = [[(N*M) for _ in range(M)] for _ in range(N)]

for i in range(N):
    seaOneLine = list(map(int, sys.stdin.readline().split()))
    sea.append(seaOneLine)
    for idx, j in enumerate(seaOneLine):
        if j == 0:
            queue.append([i, idx]) # queue에 상어 없는 위치 넣기
        else:     
            shark.append([i, idx]) # shark에 상어 위치 넣기      
            distance[i][idx] = 0     

# 어떤 방식이 효율적일까?
# 1. 그냥 상어가 없는 부분을 queue에 넣어서 제일 가까운 상어 찾기 ✅
# 2. 상어가 있는 부분을 queue에 넣기
    # 2-1. 다시 queue에 삽입
    # 2-2. 그냥 while문으로 탐색 

# 0 0 1 0
while(queue):
    x, y = queue.popleft()
    for i in shark:
        distance_x = abs(i[0]-x)
        distance_y = abs(i[1]-y)
        distance[x][y] = min(distance[x][y], max(distance_x, distance_y))

max_distance = 0
max_index = []
for idx, i in enumerate(distance):
    max_distance = max(max_distance, max(i))
    
print(max_distance)    
    