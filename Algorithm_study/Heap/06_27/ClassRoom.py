# Heap [강의실]
# https://www.acmicpc.net/problem/1374

# 소요시간 : 30분 

import heapq
import sys

def solution():
    N = int(input())
    Class = [] # 수업 정보 List
    end_heap = [] # 끝나는 시간 저장해두는 Heap
    
    # List로 입력 받기
    for i in range(N):
        a,b,c = map(int, sys.stdin.readline().split())
        Class.append([a,b,c])
    
    Class = sorted(Class, key=lambda x:(x[1])) # 시작 시간 기준으로 정렬
    
    # 끝나는 시간만 Heap에 저장
    for i in Class:
        heapq.heappush(end_heap, i[2])
        
    count = 0
    now_end = 0
    
    # 원본 List
    for i in Class:
        # now_end 초기화 되었다면 -> 기존의 강의실 사용함 -> 끝나는 시간 중 빠른 시간 가져오기
        if now_end == 0:
            pop = heapq.heappop(end_heap)
            now_end = pop
        
        # 시작 시간 < 끝나는 시간 (새 강의실 사용해야함) 
        if i[1] < now_end:
            count += 1
        
        # 기존의 강의실을 사용 할 수 있다면, now_end 시간 초기화
        else:
            now_end = 0

    return count

print(solution())