# Brute Force [피로도]
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 소요시간 : 12분

from itertools import permutations 
def solution(k, dungeons):
    answer = -1
    
    # 3가지라면, 1,2,3 중 모든 경우의 수를 구함
    list_permutations = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    
    for i in list_permutations:
        now = k
        now_highest = 0
        
        # 몇 번째 모험까지 떠날 수 있는 지 계산
        for j in i:
            if now >= dungeons[j][0]:
                now -= dungeons[j][1]
                now_highest += 1
            else:
                break
        
        # 최고 기록 갱신
        if now_highest > answer:
            answer = now_highest
            
            # 중간에 최고기록이라면 여기서 그만
            if answer == len(dungeons):
                return answer
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))