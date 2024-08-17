# DP [1로 만들기]
# https://www.acmicpc.net/problem/1463

# ⏰ 소요시간 : 60분 (포기?)

n = int(input())

# DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍 진행(bottom-up)
for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

# 결과 출력
print(d[n])

# import sys

# memo = dict()
# count = 0
# list = []
# X = int(sys.stdin.readline())

# def iscontinue(num, count):
#     global memo
#     try:
#         if memo[num] > count:
#             return False
#         else:
#             memo[num] = count
#             return True
    
#     except KeyError:
#         memo[num] = count
#         return True    

# def func_3(num, count):
#     global list, memo
#     if iscontinue(num, count):
#         if num == 1:
#             list.append(count)
#             return
        
#         elif memo[num] < count:
#             return 
        
#         elif num % 3 == 0:
#             count += 1
#             temp = num//3
#             if temp % 3 == 0:
#                 func_3(temp, count)
#             if temp % 2 == 0:
#                 func_2(temp, count)
#             func_1(temp, count)
        
#         else:
#             return 
#     else:
#         return 

# def func_2(num, count):
#     global list, memo
#     if iscontinue(num, count):
#         if num == 1:
#             list.append(count)
#             return
        
#         elif memo[num] < count:
#             return 
        
#         elif num % 2 == 0:
#             count += 1
#             temp = num// 2
#             if temp % 3 == 0:
#                 func_3(temp, count)
#             if temp % 2 == 0:
#                 func_2(temp, count)
#             func_1(temp, count)
        
#         else: 
#             return
        
#     else:
#         return 

# def func_1(num, count):
#     global list, memo
#     if iscontinue(num, count):
#         if num == 1:
#             list.append(count)
#             return
        
#         elif memo[num] < count:
#             return 
        
#         count += 1
#         temp = num-1
#         if temp % 3 == 0:
#             func_3(temp, count)
#         if temp % 2 == 0:
#             func_2(temp, count)
#         func_1(temp, count)

#     else:
#         return  

# if X % 3 == 0:
#     func_3(X, 0)

# if X % 2 == 0:
#     func_2(X, 0)

# func_1(X, 0)

# print(list)
# print(min(list))