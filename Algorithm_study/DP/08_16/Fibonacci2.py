# DP [피보나치 2]
# https://www.acmicpc.net/problem/2748

# ⏰ 소요시간 : 5분

import sys

N = int(sys.stdin.readline())
fibo_dict = dict()
fibo_dict[0] = 0
fibo_dict[1] = 1

def fibo(N):
    # Memoization이 되어있는가
    try:
        return fibo_dict[N]
    
    # 그렇지 않으면 값 구함
    except KeyError:
        fibo_num = fibo(N-1) + fibo(N-2)
        fibo_dict[N] = fibo_num
        return fibo_num
    
print(fibo(N))