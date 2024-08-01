# Greedy [섬 연결하기]
# https://school.programmers.co.kr/learn/courses/30/lessons/42861

# ⏰ 소요시간 : 20분

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX != rootY:
        parent[rootY] = rootX

def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])  # 간선을 비용 기준으로 오름차순 정렬
    
    total_cost = 0
    for cost in costs:
        x, y, weight = cost
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            total_cost += weight
            
    return total_cost

# 테스트
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))  # 4