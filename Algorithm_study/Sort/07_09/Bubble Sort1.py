# Sort [알고리즘 수업 - 버블 정렬 1]
# https://www.acmicpc.net/problem/23968

# 소요시간 : 5분 
import sys

def bubble_sort():
    input = sys.stdin.read
    reads = input().split()    
    N = int(reads[0])
    K = int(reads[1])
    A = list(map(int, reads[2:]))
    # N, K = map(int, sys.stdin.readline().split())
    # A = list(map(int, sys.stdin.readline().split()))
    for last in range(N-1,0,-1):
        for i in range(0, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                K-=1
                if not K:
                    print(A[i], A[i+1])
                    return
    
    print(-1)    

bubble_sort()
