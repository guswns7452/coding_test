# Sort [회의실 배정]
# https://www.acmicpc.net/problem/1931

# 소요시간 : Timeless.. 

import sys

num = int(sys.stdin.readline())
list_meeting = []
endPoint = 0
answer = 0

# 입력 받음
for i in range(num):
    list_meeting.append(list(map(int, sys.stdin.readline().split())))

list_meeting = sorted(list_meeting, key=lambda x:(x[1], x[0]))

print(list_meeting)

for newStart, newEnd in list_meeting:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd

print(answer)    