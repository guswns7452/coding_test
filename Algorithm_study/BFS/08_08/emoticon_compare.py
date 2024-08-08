# BFS [이모티콘]
# https://www.acmicpc.net/problem/14226

# ⏰ 소요시간 : 120분

import math
from collections import deque

def my(N):
    emo = [0, 0, 2, 3, 4, 5, 5, 7, 6, 6, 7] # 12까지 구한 값
    emo += [1000000 for _ in range(1000)]

    def findEmo(S, index_num):
        list = [] # 약수를 구함
        for i in range(2, int(math.sqrt(index_num))+1):
            if index_num % i == 0:
                list.append([index_num//i, i])
        
        for j in list:
            findEmo(S, j[0])
            
            emo[index_num] = min(emo[index_num], emo[j[0]] + j[1])
            
        if index_num <= S+1 and emo[index_num+1] == 1000000:
            findEmo(S, index_num+1)
        
        emo[index_num] = min(emo[index_num], emo[index_num+1] + 1)
        
    S = N

    if emo[S] != 1000000:
        return (emo[S])
        
    else:
        findEmo(S, S)
        return emo[S]
    
def yours(S):
    n = S
    dist = [[-1]* (n+1) for _ in range(n+1)]
    q = deque()
    q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
    dist[1][0] = 0
    while q:
        s,c = q.popleft()
        if dist[s][s] == -1: # 방문하지 않았으면
            dist[s][s] = dist[s][c] + 1
            q.append((s,s))
        if s+c <= n and dist[s+c][c] == -1:
            dist[s+c][c] = dist[s][c] + 1
            q.append((s+c, c))
        if s-1 >= 0 and dist[s-1][c] == -1:
            dist[s-1][c] = dist[s][c] + 1
            q.append((s-1, c))
    answer = -1
    for i in range(n+1):
        if dist[n][i] != -1:
            if answer == -1 or answer > dist[n][i]:
                answer = dist[n][i]
    return answer
    
for i in range(2,1001):
    m = my(i)
    y = yours(i) 
    if m != y:
        print(i, m, y)