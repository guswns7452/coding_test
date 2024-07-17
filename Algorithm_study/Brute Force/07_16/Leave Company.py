# Brute Force [퇴사]
# https://www.acmicpc.net/problem/14501

# 소요시간 : 32분

# 10
# 5 50 - O (50 + 40)
# 4 40 - O (40 + 40)
# 3 30 - O (30 + 40)
# 2 20 - O (20 + 40)
# 1 10 - O (10 + 40)
# 1 10 - O (10 + 30)
# 2 20 - O (20)
# 3 30 - O (30)
# 4 40 - X
# 5 50 - X

import sys
N = int(sys.stdin.readline())
list = []
for i in range(N):
    time, pay = map(int, sys.stdin.readline().split())
    list.append([time, pay])

for j in range(N-1, -1, -1):
    
    # 당일 상담은 가능한데, 그 이후에 없을 때
    if (j == N-1 and list[j][0] == 1) or (list[j][0] + j == N):
        list[j].append(list[j][1])
    
    # 당일 상담도 불가하고, 그 이후에 가능한 상담이 없을 때
    elif list[j+list[j][0]:] == []:
        list[j].append(0)
    
    # 당일 상담 가능 + 그 이후 상담 가능
    else:
        list[j].append(list[j][1] + max(list[j+list[j][0]:], key=lambda x:x[2])[2])
    
print(max(list, key=lambda x:x[2])[2])