# DFS [연결 요소의 개수]
# https://www.acmicpc.net/problem/11724

# ⏰ 소요시간 : 7분

import sys
from collections import deque

# 탐색할 노드 찾기
def find_start_node(visited):
    return visited.index(False)

# DFS
def dfs(graph, N):
    visited = [False for _ in range(N)]
    need_visited = deque()
    visited_count = len(visited)
    
    # 시작 노드 설정해주기
    need_visited.append(find_start_node(visited))

    total = 0
    while visited_count:
        # 방문이 필요한 리스트가 아직 존재한다면
        while need_visited:
            
            # 시작 노드를 지정하고
            node = need_visited.pop()

            # 만약 방문한 리스트에 없다면
            if visited[node] == False:
                # 방문 리스트에 노드를 추가
                visited[node] = True
                visited_count -= 1
                
                # 인접 노드들을 방문 예정 리스트에 추가
                need_visited.extend(graph[node])

        total += 1
        if visited_count:
            need_visited.append(find_start_node(visited))

    return total


N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]   # 인접 리스트

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1-1].append(node2-1)
    graph[node2-1].append(node1-1)

print(dfs(graph, N))
