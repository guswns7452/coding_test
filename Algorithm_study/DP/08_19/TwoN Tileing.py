# DP [2 x N 타일링]
# https://www.acmicpc.net/problem/11726

# ⏰ 소요시간 : 16분

import sys

n = int(sys.stdin.readline())
dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
    
print(dp[n]%10007)