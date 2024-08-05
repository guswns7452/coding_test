# BFS [타겟 넘버]
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# ⏰ 소요시간 : 15분

from collections import deque

def solution(numbers, target):
    list_leaves = deque([0])
    
    for i in numbers:
        temp = []
        while(list_leaves):
            now = list_leaves.popleft()
            temp.append(now - i)
            temp.append(now + i)
        list_leaves = deque(temp)
    
    return list_leaves.count(target)

print(solution([1,1,1,1],3))