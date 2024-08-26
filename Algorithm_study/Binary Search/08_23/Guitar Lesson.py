# 이진 탐색 [기타 레슨]
# https://www.acmicpc.net/problem/2343

# ⏰ 소요시간 : 분

import sys

N, M = map(int, sys.stdin.readline().split())
lessons = list(map(int, sys.stdin.readline().split()))
split = [-1]
aver = sum(lessons) // M

while len(split) != M:
    start, end = 0, len(lessons) - split[-1] - 2
    temp_lesson = lessons[split[-1]+1:]
    while start <= end:
        sum_value = 0
        mid = (start + end) // 2
        
        for idx, i in enumerate(temp_lesson):
            if idx < mid:
                sum_value += i
                
        if sum_value > aver:
            end = mid -1
            
        else:
            start = mid + 1
    
    split.append(split[-1] + end + 1) if abs(sum(temp_lesson[:end+1]) - aver) < abs(sum(temp_lesson[:end]) - aver) else split.append(split[-1] + end)    
    
split.append(len(lessons)-1)
max_v = 0
for idx in range(len(split)-1):
    max_v = max(max_v, sum(lessons[split[idx]+1:split[idx+1]+1]))  

print(max_v)