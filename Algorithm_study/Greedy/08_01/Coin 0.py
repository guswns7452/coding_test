# Greedy [동전 0]
# https://www.acmicpc.net/problem/11047

# ⏰ 소요시간 : 10분

import sys

N, K = map(int, sys.stdin.readline().split())

coins = [] 
count = 0
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

for i in reversed(coins):
    temp = int(K/i)
    K -= (i*temp)
    count += temp
        
print(count)