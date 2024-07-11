# Sort [알고리즘 수업 - 선택 정렬 3]
# https://www.acmicpc.net/problem/23883

# 소요시간 : 2분 

import sys

def selection_sort():
    # input = sys.stdin.read
    # reads = input().split()
    # N = int(reads[0])
    # K = int(reads[1])
    # A = list(map(int, reads[2:]))

    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split())) 
    B = sorted(A)
    
    dict_list = dict()
    for i, v in enumerate(A):
        dict_list[v] = i
    
    for last in range(N-1, 0, -1):
        max_value = B[last] # 7
        max_index = dict_list[max_value] # 0
        
        if (last != max_index):
            A[last], A[max_index] = A[max_index], A[last]
            swap_value = A[max_index]            
            dict_list[max_value], dict_list[swap_value] = last, dict_list[max_value]
            K-=1
            if not K:
                print(A[max_index], A[last])
                return
            
    print(-1)
    
selection_sort()