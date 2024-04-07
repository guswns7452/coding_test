from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' -> ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8], # 1번 노드와 연결되어 있는 노드들
    [1,7],   # 2번 노드와 연결되어 있는 노드들
    [1,4,5], # 3번 노드와 연결되어 있는 노드들
    [3,5],   # 4번
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)