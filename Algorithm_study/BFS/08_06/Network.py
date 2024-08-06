# BFS [네트워크]
# https://school.programmers.co.kr/learn/courses/30/lessons/43162 

# ⏰ 소요시간 : 23분

import copy
from collections import deque
def bfs(n, nodes):
    visited = [False for _ in range(n)]
    count = n
    queue = deque()
    network_num = 1
    
    # 처음 탐색은 0번 노드 부터
    queue.append(0)
    visited[0] = True
    count -= 1
    
    while(count):
        now_node = queue.popleft()
        for i in nodes[now_node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                count -= 1
                
        # queue가 비면, 새 시작 노드 찾아내기
        # 아직 방문하지 않은 / visited가 False인 노드
        if not queue:
            queue.append(visited.index(False))
            visited[visited.index(False)] = True
            count -= 1
            network_num += 1
            
    return network_num

def solution(n, computers):
    # 중복 연결을 방지하기 위한 List<set>으로 선언
    nodes = [set() for _ in range(n)]
    for i in computers:
        temp_list = []
        for idx, j in enumerate(i):
            if j == 1:
                temp_list.append(idx)
        
        # 인접 리스트로 변경
        for k in temp_list:
            temp = copy.deepcopy(temp_list)
            temp.remove(k)
            for t in temp:
                nodes[k].add(t)

    return bfs(n, nodes)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))