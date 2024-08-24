# DP [등굣길]
# https://school.programmers.co.kr/learn/courses/30/lessons/42898 

# ⏰ 소요시간 : 57분

def solution(m, n, puddles):
    # 갈 수 있는 곳은 0 / 없는 곳은 -1
    graph = [[0 for _ in range(m)] for _ in range(n)]
    graph[0][0] = 1
    for x, y in puddles:
        graph[y-1][x-1] = -1
    
    for idx, i in enumerate(graph):
        for idx_j, j in enumerate(i):
            if j == 0:
                if 0 <= idx-1 < n and graph[idx-1][idx_j] != -1:
                    graph[idx][idx_j] += graph[idx-1][idx_j]
                if 0 <= idx_j-1 < m and graph[idx][idx_j-1] != -1:
                    graph[idx][idx_j] += graph[idx][idx_j-1]

    return graph[n-1][m-1] % 1000000007      

print(solution(4,3,[[2,2]]))