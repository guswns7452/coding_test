# Sort [알고리즘 수업 - 병합 정렬 2]
# https://www.acmicpc.net/problem/24061

# 소요시간 : 32분

import sys
input = sys.stdin.read
reads = input().split()
N = int(reads[0])
K = int(reads[1])
list = int(reads[2:])

# N, K = map(int, sys.stdin.readline().split())
# list = list(map(int, sys.stdin.readline().split()))
isCorrect = False

def merge_sort(p, r):
    global list
    if (p < r):
        q = int((p+r)/2)
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)

def merge(p, q, r):
    global list, K, isCorrect
    i = p
    j = q + 1
    temp = []
    
    while(i <= q and j <= r):
        if (list[i] <= list[j]):
            temp.append(list[i])
            i += 1
        else:
            temp.append(list[j])
            j += 1
        
    while (i <= q):
        temp.append(list[i])
        i += 1
    while (j <= r):
        temp.append(list[j])
        j += 1
        
    i = p
    t = 0
    while (i <= r):
        list[i] = temp[t]
        i +=1; t += 1
        K -= 1
        if not K:
            print(*list)
            isCorrect = True

merge_sort(0, N-1)   
if isCorrect != True:
    print(-1)

