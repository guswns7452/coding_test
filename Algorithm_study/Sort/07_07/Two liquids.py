# Sort [두 용액]
# https://www.acmicpc.net/problem/1931

# 소요시간 : 35분

import sys

def solution():
    num = int(sys.stdin.readline())

    list_liquids = list(map(int, sys.stdin.readline().split()))
    list_liquids.sort()

    new_liquids = []
    for i in list_liquids:
        new_liquids.append([abs(i), i])
    
    new_liquids.sort()

    total = 10000000000000
    answer = [[]]
    for idx in range(len(new_liquids)-1):
        if abs(new_liquids[idx][1] + new_liquids[idx+1][1]) < total:
            total = abs(new_liquids[idx][1] + new_liquids[idx+1][1])
            answer[0] = [new_liquids[idx][1], new_liquids[idx+1][1]]
            
    answer[0].sort()
    print(answer[0][0], answer[0][1])
    
solution()
