# DP [정수 삼각형]
# https://school.programmers.co.kr/learn/courses/30/lessons/43105 

# ⏰ 소요시간 : 13분

def solution(triangle):
    length = len(triangle) - 1
    
    for idx, i in enumerate(reversed(triangle[:-1])):
        for idx_j, j in enumerate(i):
            triangle[length-idx-1][idx_j] += max(triangle[length-idx][idx_j], triangle[length-idx][idx_j+1])       
    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])