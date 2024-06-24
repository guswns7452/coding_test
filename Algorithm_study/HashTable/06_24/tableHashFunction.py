# HashTable [테이블 해시 함수]
# https://school.programmers.co.kr/learn/courses/30/lessons/147354

# 소요시간 : 28분

def solution(data, col, row_begin, row_end):
    answer = 0
    list_tuple = list()
    for i in data:
        list_tuple.append(tuple(i))
    
    # col-1 번째를 기준으로 오름차순 정렬
    # 만약 값이 같으면 첫번째 요소를 기준으로 내림차순 정렬
    list_tuple = sorted(list_tuple, key=lambda x: (x[col-1], -x[0]))
    
    S_i = list()
    for k in range(row_begin-1,row_end):
        sum = 0
        for j in list_tuple[k]:
            sum += j % (k+1)
        S_i.append(sum)
    
    # XOR 값 구하기
    answer = S_i[0]
    for t in range(1, len(S_i)):
        answer ^= S_i[t]
        
    return answer


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3

print(solution(data, col, row_begin, row_end))