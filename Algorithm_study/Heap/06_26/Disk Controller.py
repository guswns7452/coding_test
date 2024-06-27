# Heap [디스크 컨트롤러]
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

# 소요시간 : 100분 (포기)

import heapq
def solution(jobs):
    answer = 0
    length = len(jobs)
    heapq.heapify(jobs)
    time = 0
    heap = []
    while(jobs):           
        while(jobs):      #그때그때 시간에 따라 가능한 목록을 힙에 넣고
            print(1, jobs)
            x,y= heapq.heappop(jobs)
            if x>time:
                heapq.heappush(jobs,[x,y])
                print(2, jobs)
                break
            else:
                print(3, jobs)
                heapq.heappush(heap,[y,x])

        if len(heap)==0:      #힙에 아무것도 없으면 time 증가, 있다면 pop한다
            time += 1
        else:
            a,b = heapq.heappop(heap)
            answer += (a+time-b)
            time += a
    while heap:              # 남아 있는 힙 순서대로 pop
        a,b = heapq.heappop(heap)
        answer += a+time-b
        time += a
        print(time)

    return answer//length

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))