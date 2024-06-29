# Queue / Stack [올바른 괄호]
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# 소요시간 : 6분

def solution(s):
    answer = True
    bracket = []
    
    try:
        for i in s:
            if i == "(":
                bracket.append("(")
            
            elif i == ")":
                bracket.pop()
    
    except IndexError:
        return False
            
    if len(bracket):
        answer = False

    return answer

s = "()()"
print(solution(s))