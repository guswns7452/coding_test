# Heap [이중우선순위큐]
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# 소요시간 : 14분

# Python에서 힙은 최소 힙임.
# 따라서 최소값은 구할 수 있음.

# 그러면 최대 값을 pop을 하기 위해 모든 값을 다 빼고 다시 넣기 
# O(N^2logN) 인데요..?

# 차라리 리스트로 하면 더 괜찮을 듯.

def solution_1(operations):
    answer = []
    for i in operations:
        # 삽입 연산
        if i[0] == "I":
            answer.append(int(i[2:]))
        
        # 최댓값 삭제
        elif i == "D 1" and len(answer) > 0:
            answer.sort()
            answer.pop(-1)
            
        # 최솟값 삭제    
        elif i == "D -1" and len(answer) > 0:
            answer.sort()
            answer.pop(0)

    return [max(answer), min(answer)] if len(answer) > 0 else [0,0]

from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for i in arguments:
        if i == "D 1" and len(max_heap) > 0:
            heappop(max_heap)
            if len(max_heap) <= 0 or -max_heap[0] < min_heap[0]:
                min_heap = []
                max_heap = []

        elif i == "D -1" and len(min_heap) > 0:
            heappop(min_heap)
            if len(min_heap) <= 0 or -max_heap[0] < min_heap[0]:
                max_heap = []
                min_heap = []
                
        elif i[0] == "I":
            num = int(i[2:])
            heappush(max_heap,-num)
            heappush(min_heap,num)
    
    if len(min_heap) == 0:
        return [0,0]    
    
    return([-heappop(max_heap), heappop(min_heap)])

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))