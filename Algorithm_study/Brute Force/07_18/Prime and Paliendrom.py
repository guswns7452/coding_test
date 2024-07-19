# Brute Force [소수&펠린드롬]
# https://www.acmicpc.net/problem/1747

# 소요시간 : 15분

import sys

# 펠린드롬 체크하는 함수
def isPalindrome(i):
    r = reversed(str(i))
    if ''.join(r) == str(i):
        return True
    return False

# 소수 체크
def isPrime(i):
    count = 0
    # 0, 1은 소수가 아니므로, 예외 처리
    if i <= 1:
        print(2)
        sys.exit()
    
    for j in range(1, int(abs(i)**0.5)+1):
        if i % j == 0:
            count += 1
            if count > 1:
                return False
    return True
    
N = int(sys.stdin.readline())

for i in range(N,1100001):
    # 펠린드롬 인지 먼저 판단
    if isPalindrome(i):
        if isPrime(i):
            print(i)
            sys.exit()