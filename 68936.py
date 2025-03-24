## [쿼드압축 후 개수 세기]
## https://school.programmers.co.kr/learn/courses/30/lessons/68936

import copy 

def divArea(arr):
    temp = [[] for _ in range(4)]
    answer = [0, 0]
    for idx, i in enumerate(arr):
        if idx < int(len(i)/2):
            temp[0].append(i[:int(len(arr)/2)])
            temp[1].append(i[int(len(arr)/2):])
        else:
            temp[2].append(i[:int(len(arr)/2)])
            temp[3].append(i[int(len(arr)/2):])
    
    temp2 = copy.deepcopy(temp)
    
    for i in temp:
        zero_count = 0
        one_count = 0
        for idx, j in enumerate(i):
            zero_count += j.count(0)
            one_count += j.count(1)
            if zero_count and one_count:
                break
                
        if (zero_count == 0):
            temp2.remove(i)
            answer[1] += 1
            
        elif (one_count == 0):
            temp2.remove(i)
            answer[0] += 1

    return temp2, answer
    
def solution(arr):
    answer = [0, 0]

    ## 2의 몇승인지 파악하기
    for i in range(1, 11):
        if 2**i == len(arr):
            firstLength = i
    
    ## 처음에 모든 값이 같은지 체크
    zero_count = 0
    one_count = 0

    for i in arr:
        zero_count += i.count(0)
        one_count += i.count(1)

    if not zero_count:
        return [0, 1]
    elif not one_count:
        return [1, 0]
    
    # 1회 분할하기
    arr, temp_answer = divArea(arr)
    answer[0] += temp_answer[0]
    answer[1] += temp_answer[1]

    # 반복해서 분할하기
    for _ in range(firstLength-1):
        temp2_arr = []
        for i in arr:
            temp_arr, temp_answer = divArea(i)
            if len(temp_arr):
                temp2_arr += temp_arr
            
            answer[0] += temp_answer[0]
            answer[1] += temp_answer[1]
        arr = temp2_arr

    return answer

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))