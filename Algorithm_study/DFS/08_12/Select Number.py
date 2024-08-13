# DFS [숫자 고르기]
# https://www.acmicpc.net/problem/2668

# ⏰ 소요시간 : 70분

## Cycle 찾는 알고리즘

### 모든 노드에서 출발하는 알고리즘
### 분기일 때, 다음 노드가 시작 노드와 같으면 -> cycle임
### 분기일 때, 다음 노드가 시작 노드는 아닌데, 비어있다면 -> 그 경로는 cycle 아님
### 계속 경로를 기록해두어야 함

## Cycle 찾으면?
### 1. 경로가 겹침. 더 긴걸로 교체
### 2. 안겹침? 그냥 append

### 이중 list에서 계속 합쳐야겠다.

import sys

N = int(sys.stdin.readline())

# 인접 리스트로 입력 받기
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    graph[i].append(int(sys.stdin.readline()))

cycle = []    

def dfs(start_node, graph):
    global cycle
    stack = [[start_node, [start_node]]] # [현재 노드, [이동 경로]]
    visited = [False for _  in range(len(graph)+1)]
    while(stack):
        # print(start_node, stack)
        now_node, move_route = stack.pop()
        visited[now_node] = True
        
        # 더 이상 탐색 할 곳 없음
        if not len(graph[now_node]): 
            pass
        
        # 본인 스스로 사이클 이면?
        elif now_node == start_node and start_node in graph[now_node]:
            cycle.append([now_node])
            gotoNodes = graph[now_node] # 본인은 제외하고, 경로 stack에 넣기
            gotoNodes.remove(now_node)
            for i in gotoNodes:
                if not visited[i]:
                    move_route.append(i)
                    stack.append([i, move_route])
        
        # 계속 삽입
        else:
            for i in graph[now_node]:
                if not visited[i]:
                    move_route.append(i)
                    stack.append([i, move_route])
                
                # cycle 생성 됨
                elif i == start_node and len(move_route) != 1:
                    cycle.append(move_route)
                    return 

# 노드 하나씩 탐색 하기
for i in range(1, N+1):
    dfs(i, graph)
    
total = set()
sorted_list = [sorted(subList) for subList in cycle]
sorted_list.sort()

temp = [[-1, 0] for i in range(N+1)] # index, max_len()

# 토탈 경로 삽입
for idx, i in enumerate(sorted_list):
    if temp[i[0]][1] < len(i):
        temp[i[0]] = [idx, len(i)]
            
for i in temp:
    if i[0] != -1:
        for k in sorted_list[i[0]]:
            total.add(k)
        
print(len(total))
for i in sorted(list(total)):
    print(i)
    

# [ChatGPT 개선]
# 생각해보니, 어짜피 한 노드는 하나의 방향만 존재함 -> 분기가 없음! 
# 그러니 이 방법도 상관 없음

# import sys

# def dfs(start_node, graph):
#     stack = [[start_node, [start_node]]]  # [현재 노드, [이동 경로]]
#     visited = [False] * (len(graph))
#     cycles = []
    
#     while stack:
#         current_node, path = stack.pop()
#         visited[current_node] = True
        
#         next_node = graph[current_node][0]
        
#         if next_node in path:  # 사이클 발견
#             cycle_start_idx = path.index(next_node)
#             cycles.append(path[cycle_start_idx:])
#             continue
        
#         if not visited[next_node]:
#             stack.append([next_node, path + [next_node]])
    
#     return cycles

# def main():
#     N = int(sys.stdin.readline().strip())

#     # 인접 리스트로 입력 받기
#     graph = [[] for _ in range(N+1)]
#     for i in range(1, N+1):
#         graph[i].append(int(sys.stdin.readline().strip()))

#     all_cycles = []
    
#     # 노드 하나씩 탐색하여 모든 사이클을 찾기
#     for i in range(1, N+1):
#         all_cycles.extend(dfs(i, graph))
    
#     # 각 사이클에서 중복된 노드를 제거하고 결과 정렬
#     unique_nodes = set()
#     for cycle in all_cycles:
#         unique_nodes.update(cycle)
    
#     result = sorted(unique_nodes)
    
#     # 결과 출력
#     print(len(result))
#     for node in result:
#         print(node)

# if __name__ == "__main__":
#     main()