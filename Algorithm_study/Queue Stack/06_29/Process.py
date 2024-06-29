# Queue / Stack [프로세스]
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 소요시간 : 23분

def solution(priorities, location):
    answer = 0
    pri = 0
    count = 0
    while(1):
        if (priorities[0] == max(priorities)):
            priorities.pop(0)
            priorities.append(0)
            pri += 1
            if count%len(priorities) == location:
                return pri 
        
        else:
            priorities.append(priorities.pop(0))
        
        count += 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))