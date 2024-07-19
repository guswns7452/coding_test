# Brute Force [펠린드롬 만들기]
# https://www.acmicpc.net/problem/1254

# 소요시간 : 42분

# 맨 뒤 문자(a)를 가지고, index 들을 찾아냄.
# -> 재귀로 들어가야할듯? 

import sys

# SubList를 재귀로 판단
def isPalindrome(list):
    if len(list) == 1 or len(list) == 0:
        return True
    else:
        if list.pop(0) == list.pop():
            return isPalindrome(list)
        else:
            return False
        
# 입력
tempList = sys.stdin.readline().strip()
N = len(tempList)

# 맨 뒤가 펠린드롬인지만 고려함
indexs = []
for j in range(0,N-1):
    if tempList[j] == tempList[N-1]:
        indexs.append(j)
    
for k in indexs:
    if isPalindrome(list(tempList[k:])):
        print(k+N)
        sys.exit(0)

# 맨 뒤가 펠린드롬이 아니면 그냥 전부 만들어야함           
print(N*2-1)        
        