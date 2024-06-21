# HashTable [완주하지 못한 선수]
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 소요시간 : 30분 

# 실패 1 : 효율성 문제
    # Array로 하나씩 접근해서 삭제함 -> O(N^2) 으로 시간초과 
    # 1억회 당 1초라고 생각하면 됨
    # 10만의 연산 -> O(N^2) -> 100억 -> 최대 100초

def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]


# 성공 : 정렬해서 비교
    # 10만번의 연산 -> O(NlogN) -> 50만번
    # 1초 이내의 연산 가능

def solution(participant, completion):
    participant.sort() # O(NlogN)
    completion.sort() # O(NlogN)
    
    for i in range(0, len(participant)-1):
        if participant[i] != completion[i]: # 최악 : O(N)
            return participant[i]
    
    return(participant.pop())

part = ["leo", "kiki", "eden"]
com = ["eden", "kiki"]
print(solution(part, com))