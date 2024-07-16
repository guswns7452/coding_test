# Brute Force [피로도]
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 소요시간 : 12분

from itertools import permutations 
def solution(k, dungeons):
    answer = -1
    list_permutations = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    for i in list_permutations:
        now = k
        now_highest = 0
        for j in i:
            if now >= dungeons[j][0]:
                now -= dungeons[j][1]
                now_highest += 1
            else:
                break
        
        if now_highest > answer:
            answer = now_highest
            if answer == len(dungeons):
                return answer
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))