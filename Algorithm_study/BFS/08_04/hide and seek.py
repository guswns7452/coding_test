# BFS [숨바꼭질 3]
# https://www.acmicpc.net/problem/13549

# ⏰ 소요시간 : 65분
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
min_time = 10000000
len_visited = max(N, K)

def isappendable(num, time):
    global N, K, len_visited
    list_appenable = list()
    
    # num - 1
    list_appenable.append([num-1, time+1]) if num-1 > 0 else list_appenable.append(False)
        
    # num + 1    
    list_appenable.append([num+1, time+1]) if num+1 <= 2*len_visited else list_appenable.append(False)

    # 2 * num
    list_appenable.append([2*num, time]) if num <= len_visited and num > 0 else list_appenable.append(False)

    return list_appenable

def bfs(N, K):
    global min_time, len_visited
    visited = [10000000]*(2*len_visited+1)
    queue = deque()
    
    # 혹시나 같으면 바로 종료
    if N == K:
        print(0)
        sys.exit()
    
    # N이 작으면 한 칸씩 이동하는게 제일 빠름    
    elif N > K:
        print(N-K)
        sys.exit(0)
        
    for i in isappendable(N, 0):
        if i != False:
            queue.append(i)
            visited[i[0]] = i[1]
    
    while(queue):
        x, y = queue.popleft()
        # 목표 지점일 때, 최소 시간 업데이트
        if x == K:
            min_time = min(y, min_time)
        
        # 추가할 수 있는 부분만 추가하기
        for i in isappendable(x, y):
            if i != False:
                visited[i[0]] = min(visited[i[0]], i[1]) 
                if visited[i[0]] == i[1]:
                    queue.append(i)
        
    return visited[K]   

print(bfs(N,K))