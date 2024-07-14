# Brute Force [모의고사]
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 소요시간 : 12분

def solution(answers):
    answers_len = len(answers) 
    
    answer = []
    one = [1,2,3,4,5] * (int(answers_len/5) + 1)
    two = [2,1,2,3,2,4,2,5] * (int(answers_len/8) + 1)
    three = [3,3,1,1,2,2,4,4,5,5] * (int(answers_len/10) + 1)
    
    count = [0,0,0]
    for i, one_, two_, three_ in zip(answers, one, two, three):
        if i == one_:
            count[0] += 1
        if i == two_:
            count[1] += 1
        if i == three_:
            count[2] += 1
    
    max = 0        
    for idx, k in enumerate(count):
        if k > max:
            answer = [0]
            answer[0] = idx + 1
            max = k
        elif k == max:
            answer.append(idx + 1)
            
    return answer

print(solution([1,3,2,4,2]))