# Sort [알고리즘 수업 - 선택 정렬 1]
# https://www.acmicpc.net/problem/23881

# 소요시간 : 10분 

import sys

input = sys.stdin.read
reads = input().split()
N = int(reads[0])
K = int(reads[1])
A = list(map(int, reads[2:]))

# N, K = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))

def selection_sort(list):
    global N, K 
    for last in range(N-1, 0, -1):
        max_value = max(list[:last+1])
        max_index = list.index(max_value)
        if (last != max_index):
            list[last], list[max_index] = list[max_index], list[last] 
            K-=1
            if not K:
                print(list[max_index], list[last]) 
                return
            
    print(-1)
    
selection_sort(A)