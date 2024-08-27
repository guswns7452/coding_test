# 이진 탐색 [입국 심사]
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# ⏰ 소요시간 : 26분

def solution(n, times):
    start, end = 1, max(times) * n
    while start <= end:
        print(start, end)
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time
        
        if total >= n:
            end = mid - 1
        else:
            start = mid + 1
    return end + 1
