# 이진 탐색 [랜선 자르기]
# https://www.acmicpc.net/problem/1654

# ⏰ 소요시간 : 16분

## 802 / 743 / 457 / 539
import sys

K, N = map(int, sys.stdin.readline().split())
wlan = []
for i in range(K):
    wlan.append(int(sys.stdin.readline()))

start, end = 0, sum(wlan)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in wlan:
        if mid == 0:
            total += i
            continue            
        total += i//mid
    
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)