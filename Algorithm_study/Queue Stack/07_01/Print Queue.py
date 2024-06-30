# Queue / Stack [프린터 큐]
# https://www.acmicpc.net/problem/1966

# 소요시간 : 14분
import sys

def solution():
    T = int(input())
    for i in range(T):
        N, location = map(int, input().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        
        pri = 0
        count = 0
        while(1):
            if (priorities[0] == max(priorities)):
                priorities.pop(0)
                priorities.append(0)
                pri += 1
                if count%len(priorities) == location:
                    print(pri)
                    break
            
            else:
                priorities.append(priorities.pop(0))
            
            count += 1

solution()