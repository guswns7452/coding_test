# HashTable [의상]
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 소요 시간 : 50분

# 시도1 : 아마 Combination에서 시간 초과가 난듯.
import itertools

def listToDict(clothes):
    clo_dict = dict()
    for i in clothes:
        if clo_dict.get(i[1]) != None:
            sub_list = clo_dict.get(i[1])
            sub_list.append(i[0])
            clo_dict[i[1]] = sub_list
        
        else:
            sub_list = list()
            clo_dict[i[1]] = sub_list
            
    return clo_dict

def solution(clothes):
    clo_dict = listToDict(clothes)
    
    keys = clo_dict.keys()
    sum = 0
    for i in range(len(keys),0,-1):
        nCr = itertools.combinations(keys, i) # O(2^N)
        if i == 1:
            return (sum + len(clothes))
        
        for i in nCr:
            multi = 1
            for j in i:
                multi *= len(clo_dict.get(j))
            sum += multi
    
    return sum

# 시도 2

def listToDict(clothes):
    clo_dict = dict()
    for i in clothes:
        if i[1] in clo_dict.keys():
            clo_dict[i[1]] += [i[0]]
        
        else:
            clo_dict[i[1]] = [i[0]]
            
    return clo_dict

def solution(clothes):
    closet = listToDict(clothes)
    print(closet)
    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수 (N+1)(M+1)
    answer = 1
    
    for _, value in closet.items():
        answer *= (len(value) + 1)
    
    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))