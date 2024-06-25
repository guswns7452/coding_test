# Heap [더 맵게]
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 소요시간 : 15분

import heapq

def solution(scoville, K):
    h = []
    answer = 0
    
    # 차례대로 힙에 삽입
    for i in scoville:
        heapq.heappush(h, i)
    
    while (1):
        new_scoville = 0
        first = heapq.heappop(h)
        
        # 가장 작은 수가 K보다 크면 Return
        if first >= K:
            return answer
        
        # 만약 Heap에서 다 빼서, 힙이 비었으면 -1 Return
        elif len(h) == 0: 
            return -1
        
        new_scoville = first + (heapq.heappop(h) * 2)
        heapq.heappush(h, new_scoville)
        answer += 1

def solution_list(scovile, k):
    answer = 0
    
    while(1):
        new_scovile = 0
        
        # 최소값 찾기 : O(N)
        # index 찾기 : O(N)
        first = scovile.pop(scovile.index(min(scovile)))
        
        if first >= k:
            return answer

        elif len(scovile) == 0: 
            return -1
        
        new_scovile = first + (scovile.pop(scovile.index(min(scovile))) * 2)
        scovile.append(new_scovile)
        answer += 1
        
scoville = [1,2,3,9,10,12]
k = 7
print(solution_list(scoville, k))