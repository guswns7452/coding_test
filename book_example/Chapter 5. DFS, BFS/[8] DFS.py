## DFS : 깊이 우선 탐색 (그래프에서 깊은 부분을 우선적으로 탐색)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' -> ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)