# Sort [알고리즘 수업 - 퀵 정렬 3]
# https://www.acmicpc.net/problem/24092

# 소요시간 : 

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read
reads = input().split()
N = int(reads[0])
A = list(map(int, reads[1:N+1]))
B = list(map(int, reads[N+1:]))

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# B = list(map(int, sys.stdin.readline().split()))
isCorrect = False

def quick_sort(p, r):
    global A
    if (p < r):
        q = partition(p, r)
        quick_sort(p, q - 1)
        quick_sort(q + 1, r)

def partition(p, r):
    global A, B, isCorrect
    x = A[r] # Pivot
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            if A[i] == B[i]:
                if A == B:
                    print(1)
                    isCorrect = True
                    sys.exit(0)
    
    A[i + 1], A[r] = A[r], A[i + 1]
    if A[i+1] == B[i+1] and A[r] == B[r]:
        if A == B:
            print(1)
            isCorrect = True
            sys.exit(0)
    return i + 1

if A == B:
    print(1)
    isCorrect = True
else:
    quick_sort(0, N-1)

if isCorrect == False:
    print(0)