# Greedy [구명보트]
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# ⏰ 소요시간 : 40분

def solution(people, limit):
    answer = 0
    people.sort() # O(NlogN)
    min_index = 0
    max_index = len(people) - 1
    
    # 두 인덱스가 뒤 바뀔때 까지
    while(min_index < max_index): # O(N)
        if people[min_index] + people[max_index] <= limit:
            min_index += 1
            max_index -= 1
            answer += 1
        
        else:
            max_index -= 1
    
    answer += len(people) - (answer*2)
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))