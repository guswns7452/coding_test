# 이진 탐색 [용액]
# https://www.acmicpc.net/problem/2467

# ⏰ 소요시간 : 35분

# 1 2 3 4 5 6 7 8
# 10

import sys

N = int(sys.stdin.readline())
waters = list(map(int, sys.stdin.readline().split()))

start, end = 0, len(waters)-1
answer = [abs(waters[start] + waters[end]), waters[start], waters[end]]

while start < end:
    if abs(waters[start] + waters[end]) <= answer[0]:
        answer = [abs(waters[start] + waters[end]), waters[start], waters[end]]

    if waters[start] + waters[end] < 0:
        start += 1
        
    else:
        end -= 1

answer.pop(0)       
print(* answer)