# Brute Force [소수 찾기]
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 소요시간 : 20분

# 순열로 모든 경우의 수 찾기
# 얘가 소수인지 판단하기

from itertools import permutations

def solution(numbers):
    answer = 0
    numbersList = []
    allList = []

    for i in numbers:
        numbersList.append(int(i))
        
    # 한개씩 추출해서 넣기
    allList = list(set(numbersList))    
    
    # 여러개 추출해서 넣기
    for j in range(2, len(numbers)+1):
        tempList = list(permutations(numbersList,j))
        tempList = list(set(tempList))
        
        for k in tempList:
            tempString = ""
            for t in k:
                tempString += str(t)
            
            allList.append(int(tempString))    
    
    allList = list(set(allList))
    
    # 소수인지 파악하기
    for i in allList:
        count = 0
        
        if i == 1:
            continue
        
        for j in range(1, int(abs(i)**0.5) + 1):
            if i % j == 0:
                count += 1
            
        if count == 1:
            answer += 1
            
    return answer


numbers = "011"
print(solution(numbers))