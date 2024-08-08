# BFS [이모티콘]
# https://www.acmicpc.net/problem/14226

# ⏰ 소요시간 : 120분

import math
import sys
sys.setrecursionlimit(10**6)

emo = [0, 0, 2, 3, 4, 5, 5, 7, 6, 6, 7] # 12까지 구한 값
emo += [1000000 for _ in range(1000)]

def findEmo(S, index_num):
    list = [] # 약수를 구함
    for i in range(2, int(math.sqrt(index_num))+1):
        if index_num % i == 0:
            list.append([index_num//i, i])
    
    for j in list:
        # if emo[j[0]] == 1000000:
        findEmo(S, j[0])
        
        emo[index_num] = min(emo[index_num], emo[j[0]] + j[1])
        
    if index_num <= S+1 and emo[index_num+1] == 1000000:
        findEmo(S, index_num+1)
    
    emo[index_num] = min(emo[index_num], emo[index_num+1] + 1)
    
S = int(input())

if emo[S] != 1000000:
    print(emo[S])
    
else:
    findEmo(S, S)
    print(emo[S])