# BFS [A → B]
# https://www.acmicpc.net/problem/16953

# ⏰ 소요시간 : 7분

import sys

A, B = map(int, sys.stdin.readline().split())
count = 0

while(B > A):
    count += 1
    if B%10 == 1:
        B //= 10
    elif B%2 == 0:
        B //= 2
    else:
        print(-1)
        sys.exit()
    
if A == B:
    print(count+1)
    
else:
    print(-1)