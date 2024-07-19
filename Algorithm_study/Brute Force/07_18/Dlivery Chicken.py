# Brute Force [치킨 배달]
# https://www.acmicpc.net/problem/15686

# 소요시간 : 75분

# 치킨 집 기준으로 생성

# 치킨 집 기준
# {
#   (2,3) : [[(1,3),1]] 
#   (3,3) : [[(1,3),2]]
#   (5,5) : [[(1,3),6]]
# }

# 집 기준 -> 폐업 시키고 나서 Update -> Values
# {
#   (1,3) : 1 
#   (3,3) : 
#   (5,5) : 
# }

# Total Length
# 

import sys, copy
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
house_chicken = list()
for i in range(N):
    house_chicken.append(list(map(int, sys.stdin.readline().split())))

# 치킨집 리스트 뽑아내기
chicken = dict()
for idx, val in enumerate(house_chicken):
    for idx_j, val_j in enumerate(val):
        if val_j == 2:
            chicken[(idx, idx_j)] = []
            
# 집 - 치킨집 거리 구하기
house = dict()
total_length = 0
for idx, val in enumerate(house_chicken):
    for idx_j, val_j in enumerate(val):
        if val_j == 1:
            house[idx, idx_j] = 0
            for k in chicken.keys():
                chicken[k].append([(idx, idx_j), abs(k[0]-idx) + abs(k[1]-idx_j)])

# 폐업 안하면
if len(chicken.keys())-M == 0:
    for i in chicken.items():
        keys = i[0]
        values = i[1]
        for k in values:
            if house[k[0]] == 0:
                house[k[0]] = k[1]
                total_length += k[1]
            elif house[k[0]] > k[1]:
                total_length += k[1] - (house[k[0]])
                house[k[0]] = k[1]

            
# 폐업하는 경우의 수
else:
    all_closed = list(combinations(chicken.keys(), len(chicken.keys())-M))
    for i in all_closed:
        copy_chicken = copy.deepcopy(chicken)
        copy_house = copy.deepcopy(house)
        temp_total_length = 0
        for j in i:
            copy_chicken.pop(j)
            
        for t in copy_chicken.items():
            keys = t[0]
            values = t[1]
            for k in values:
                if copy_house[k[0]] == 0:
                    copy_house[k[0]] = k[1]
                    temp_total_length += k[1]
                        
                elif copy_house[k[0]] > k[1]:
                    temp_total_length += k[1] - (copy_house[k[0]])
                    copy_house[k[0]] = k[1]
        
        if total_length == 0:
            total_length = temp_total_length
        elif total_length > temp_total_length:
            total_length = temp_total_length
            
print(total_length)