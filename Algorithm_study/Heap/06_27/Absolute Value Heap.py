# Heap [절대값 힙]
# https://www.acmicpc.net/problem/11286

# 소요시간 : 45분


import heapq
import sys

def solution():
    N = int(input())
    
    # [Map] { "입력 값" : "현재 입력 받은 횟수" }
    check_dict = dict()
    heap = []
    
    for i in range(N):
        num = int(sys.stdin.readline())
        
        # 삽입 연산
        if num != 0:
            try:
                check_dict[num] = check_dict[num] + 1
            except:
                check_dict[num] = 1
            
            heapq.heappush(heap, abs(num)) # 절대 값을 Heap에 넣음
        
        # pop 연산    
        elif num == 0:
            popNum = 0
            try:
                popNum = heapq.heappop(heap)
                if check_dict[-popNum] > 0 : # Map에 음수를 체크함
                    check_dict[-popNum] = check_dict[-popNum] - 1
                    print(-popNum)

                elif check_dict[popNum] > 0: # Map에 양수를 체크함
                    check_dict[popNum] = check_dict[popNum] - 1
                    print(popNum)
            
            # Heap이 비었다면    
            except IndexError: 
                print(0)
            
            # 음수가 없으면 양수 체크
            except KeyError:
                if check_dict[popNum] > 0:
                    check_dict[popNum] = check_dict[popNum] - 1
                    print(popNum)

solution()