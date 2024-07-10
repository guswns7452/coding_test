# Sort [알고리즘 수업 - 버블 정렬 3]
# https://www.acmicpc.net/problem/23970

# 소요시간 : 12분 
import sys

input = sys.stdin.read
reads = input().split()    
N = int(reads[0])
A = list(map(int, reads[1:N+1]))
B = list(map(int, reads[N+1:]))
    
def bubble_sort():
    
    for last in range(N-1,0,-1):
        for i in range(0, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                if A[i+1] == B[i+1]:
                    if A == B:
                        print(1)
                        return
    
    print(0)    

if A == B:
    print(1)
    sys.exit(0)
else:
    bubble_sort()
