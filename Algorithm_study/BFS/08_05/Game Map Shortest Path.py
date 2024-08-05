# BFS [게임 맵 최단거리]
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# ⏰ 소요시간 : 35분

from collections import deque

def solution(maps):
    len_x, len_y = len(maps), len(maps[0])
    visited = [[(len_x*len_y+1) for _ in range(len_y)] for _ in range(len_x)] 
    queue = deque([[0,0,1]])
    visited[0][0] = 1
    
    while(queue):
        x, y, now = queue.popleft()
        
        # 상
        if 0 <= x-1 and maps[x-1][y] != 0 and visited[x-1][y] > now+1:
            queue.append([x-1, y, now+1])
            visited[x-1][y] = now+1
        
        # 하
        if x+1 < len_x and maps[x+1][y] != 0 and visited[x+1][y] > now+1:
            queue.append([x+1, y, now+1])
            visited[x+1][y] = now+1
        
        # 좌
        if 0 <= y-1 and maps[x][y-1] != 0 and visited[x][y-1] > now+1:
            queue.append([x, y-1, now+1])
            visited[x][y-1] = now+1
        
        # 우
        if y+1 < len_y and maps[x][y+1] != 0 and visited[x][y+1] > now+1:
            queue.append([x, y+1, now+1])
            visited[x][y+1] = now+1
        
    return visited[len_x-1][len_y-1] if visited[len_x-1][len_y-1] != len_x*len_y+1 else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))