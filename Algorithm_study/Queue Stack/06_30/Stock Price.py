# Queue / Stack [주식 가격]
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 소요시간 : 10분

def solution(prices):
    answer = []
    for i, v in enumerate(prices):
        
        for j in range(i+1, len(prices)):
            if v > prices[j]:
                answer.append(j-i)
                break
            
        if(i+1 != len(answer)):
            answer.append(len(prices)-i-1)
    return answer

print(solution([1, 2, 3, 2, 3]))