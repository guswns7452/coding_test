from collections import deque
import copy

def bfs(start_node, graph):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        curr_node = queue.popleft()

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return len(visited)

def solution(n, wires):
    answer = n
    tree = dict()
    
    # 인접 리스트로 변경
    for i in range(1,n+1):
        tree[i] = []
    for i in wires:
        tree[i[0]].append(i[1])
        tree[i[1]].append(i[0])
    
    
    # 한개씩 연결을 끊으며 갯수 파악하기
    for j in wires:
        temp_tree = copy.deepcopy(tree)
        temp_tree[j[0]].remove(j[1])
        temp_tree[j[1]].remove(j[0])
        value = abs(bfs(j[0], temp_tree) - bfs(j[1], temp_tree))
        if value < answer:
            answer = value
    return answer


print(solution(4, [[1,2],[2,3],[3,4]]))