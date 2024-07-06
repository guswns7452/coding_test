# Sort [가장 큰 수]
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 소요시간 : 57분 

from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    def compare(a, b):
        a = str(a)
        b = str(b)
        
        # 그리디 개념 적용
        s1 = int(a + b)
        s2 = int(b + a)
        
        if s1 < s2:
            return 1
        elif s1 > s2:
            return -1
        else:
            return 0
    
    numbers.sort(key=cmp_to_key(compare))
    
    # 00, 000 같은 경우를 고려한 형변환
    answer = str(int("".join(map(str, numbers))))
    
    return answer

def sortList(list):
    # 32 315 31 310 3 30 
    list = sorted(list, key=lambda x:(x//(10**(len(str(x))-2))), reverse=True)
    for i in range(len(list)-1):
        a = str(list[i])
        b = str(list[i+1])
        s1 = int(a + b) 
        s2 = int(b + a) 
        if s1 < s2:
            list[i], list[i+1] = list[i+1], list[i]
            
    return list
            
def solution(numbers):
    answer = ''
    diction = dict()
    for i in numbers:
        tempList = diction.get(i//(10**(len(str(i))-1)))
        if tempList == None:
            tempList = []
            tempList.append(i)
        else:
            tempList.append(i)
        diction[i//(10**(len(str(i))-1))] = tempList
    
    for i in sorted(diction,reverse=True):
        for i in sortList(diction.get(i)):
            print(i)
            answer += str(i)
    
    print(diction)
    return answer

print(solution([555, 565, 566, 55, 56, 5, 54, 544, 549]))