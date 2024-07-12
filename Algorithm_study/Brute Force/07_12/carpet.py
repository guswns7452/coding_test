# Brute Force [카펫]
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 소요시간 : 19분

def solution(brown, yellow):
    answer = []
    pairs = []
    
    # 곱해서 나올 수 있는 경우의 수 찾기
    for i in range(1, int(abs(yellow)**0.5) + 1):
        if yellow % i == 0:
            pairs.append((yellow // i, i))

    for j in pairs:
        if (((j[0] + 2) * 2) + (j[1] * 2)) == brown:
            answer.append(j[0]+2)
            answer.append(j[1]+2)
            return answer

print(solution(24,24))

