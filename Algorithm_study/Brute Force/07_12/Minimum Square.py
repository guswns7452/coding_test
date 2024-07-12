# Brute Force [최소직사각형]
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

# 소요시간 : 29분

def solution(sizes):
    answer = 0
    # 둘 중에 큰 값을 앞으로 밀기
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    
    # max 값 찾기
    max_width = 0
    max_height = 0
    for j in sizes:
        if j[0] > max_width:
            max_width = j[0]
        if j[1] > max_height:
            max_height = j[1]
    
    answer = max_height * max_width
    return answer


print(solution(sizes=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))