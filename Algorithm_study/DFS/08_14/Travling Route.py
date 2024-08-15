# DFS [여행 경로]
# https://school.programmers.co.kr/learn/courses/30/lessons/43164#

# ⏰ 소요시간 : 70분

import copy
from collections import deque

def dfs_recursive(graph, current, route, count):
    # 모든 경로를 다 탐색한 경우
    if len(route) == count + 1:
        return route
    
    # 현재 노드에서 갈 수 있는 다음 목적지들을 탐색
    if current in graph:
        next_nodes = sorted(graph[current])  # 알파벳 순서로 정렬
        for i, next_node in enumerate(next_nodes):
            # 다음 목적지를 선택했으므로 해당 목적지를 제거
            graph_copy = copy.deepcopy(graph)
            graph_copy[current].pop(i)
            result = dfs_recursive(graph_copy, next_node, route + [next_node], count)
            if result:  # 유효한 경로를 찾은 경우
                return result
    
    return None  # 유효한 경로를 찾지 못한 경우
        
def solution(tickets):
    answer = ['ICN']
    count = len(tickets)
    graph = dict()
    for depart, arrival in tickets:
        try:
            graph[depart].append(arrival)
        
        except KeyError:
            graph[depart] = [arrival]
    

    # 정렬
    for i in graph.keys():
        graph[i].sort()
        
    return dfs_recursive(graph, "ICN", ["ICN"], count)

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])