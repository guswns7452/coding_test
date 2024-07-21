# Greedy [체육복]
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 소요시간 : 20분

import copy
def solution(n, lost, reserve):
    # 여분 가져온 애가 도난당함
    copy_reserve = copy.deepcopy(reserve)
    for j in reserve:
        if j in lost:
            copy_reserve.remove(j)
            lost.remove(j)
    
    reserve = copy_reserve        
    answer = n-len(lost)
    
    lost.sort()
    reserve.sort()
    
    # 빌려주는 과정
    for i in lost:
        if i == 1 and i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        
        elif i == n and i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        
        elif i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
        
    return answer

print(solution(10, [1, 2, 3, 4, 5, 6], [1, 2, 3]))