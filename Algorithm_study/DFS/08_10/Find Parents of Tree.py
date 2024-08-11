# DFS [트리의 부모 찾기]
# https://www.acmicpc.net/problem/11725

# ⏰ 소요시간 : 12분

import sys
from collections import deque

# DFS
def dfs(graph, N):
    visited = [False for _ in range(N)]
    need_visited = deque()
    parents = [1 for _ in range(N-1)]
    
    # 시작 노드 설정해주기
    need_visited.append(0)

    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
            
        # 시작 노드를 지정하고
        node = need_visited.pop()

        # 만약 방문한 리스트에 없다면
        if visited[node] == False:
            # 방문 리스트에 노드를 추가
            visited[node] = True
                
            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
            for i in graph[node]:
                if visited[i] == False:
                    parents[i-1] = node + 1
                
    return parents

N = int(sys.stdin.readline())

graph = [[] for _ in range(N)]   # 인접 리스트

for _ in range(N-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1-1].append(node2-1)
    graph[node2-1].append(node1-1)

for i in dfs(graph, N):
    print(i)
