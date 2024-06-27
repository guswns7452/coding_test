# Queue / Stack [같은 숫자는 싫어]
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# 소요시간 : 6분

def solution(arr):
    answer = []
    for i in range(len(arr)):
        try:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
        
        except IndexError:
            answer.append(arr[i])
            
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))