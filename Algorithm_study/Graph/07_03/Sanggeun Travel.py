# Graph [상근이의 여행]
# https://www.acmicpc.net/problem/9372

# 소요시간 : 17분

import sys

T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    for _ in range(b):
        _, _ = map(int, sys.stdin.readline().split())
        
    print(a-1)
