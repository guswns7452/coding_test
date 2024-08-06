# BFS [토마토]
# https://www.acmicpc.net/problem/7576 

# ⏰ 소요시간 : 35분

import sys
from collections import deque

queue = deque()

# 처음 입력받은 토마토 중 1인 것들 모두 queue
def findOneTomato(nodes):
    queue = deque()
    for idx, i in enumerate(nodes):
        for idx_j, j in enumerate(i):
            if j == 1:
                queue.append([idx, idx_j])
    return queue

def countZero(nodes):
    total = 0
    for i in nodes:
        total += i.count(0)
    return total
        
M, N = map(int, sys.stdin.readline().split())
nodes = []

for _ in range(N):
    nodes.append(list(map(int, sys.stdin.readline().split())))

# 안 익은 토마토가 없으면?
ZeroNum = countZero(nodes)
if not ZeroNum:
    print(0)
    sys.exit()

# 1인 곳 찾기
queue = findOneTomato(nodes)
days = 0

# 0이 없을 때 까지 반복
while(ZeroNum):
    # queue가 비었는데 반복문이 안 끝남.    
    if not queue:
        print(-1)
        sys.exit(0)
        
    next_queue = deque()
    while(queue):
        x, y = queue.popleft()
        
        # 하
        if x+1 < N and nodes[x+1][y] == 0:
            next_queue.append([x+1, y])
            nodes[x+1][y] = 1
            ZeroNum -= 1
            
        # 상
        if x-1 >= 0 and nodes[x-1][y] == 0:
            next_queue.append([x-1, y])
            nodes[x-1][y] = 1
            ZeroNum -= 1
            
        # 우
        if y+1 < M and nodes[x][y+1] == 0:
            next_queue.append([x, y+1])
            nodes[x][y+1] = 1
            ZeroNum -= 1
            
        # 좌
        if y-1 >= 0 and nodes[x][y-1] == 0:
            next_queue.append([x, y-1])
            nodes[x][y-1] = 1 
            ZeroNum -= 1           
    
    days += 1
    queue = next_queue 
        
print(days)