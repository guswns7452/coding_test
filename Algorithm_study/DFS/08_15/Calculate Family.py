# BFS [촌수계산]
# https://www.acmicpc.net/problem/2644

# ⏰ 소요시간 : 20분

import sys
from collections import deque

N = int(sys.stdin.readline())
goto1, goto2 = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

line = int(sys.stdin.readline())
for _ in range(line):
    one, two = map(int, sys.stdin.readline().split())
    graph[one].append(two)
    graph[two].append(one)

def bfs(graph, start, end):
    global N
    visited = [False for _ in range(N+1)]
    queue = deque()
    queue.append([start, 0])
    visited[start] = True

    while(queue):
        nowNode, depth = queue.popleft()
        if nowNode == end:
            return depth
        
        for i in graph[nowNode]:
            if not visited[i]:
                queue.append([i, depth+1])
                visited[i] = True


    return -1

print(bfs(graph, goto1, goto2))