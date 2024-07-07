# Sort [H-Index]
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 소요시간 : 12분 

def solution(citations):
    answer = 0
    diction = dict()
    citations.sort(reverse=True)
    print(citations)
    # 6, 5, 3, 1, 0
    for i in range(len(citations), -1, -1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count >= i:
            return i
                
    return answer

citations = [46, 328, 8344, 164, 1]
print(solution(citations))