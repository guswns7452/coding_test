# DP [계단 오로기]
# https://www.acmicpc.net/problem/2579

# ⏰ 소요시간 : 분

import sys

Stairs = int(sys.stdin.readline())
point_list = list()

for i in range(Stairs):
    num = int(sys.stdin.readline())
    if i == 0: 
        point_list.append([num, num, False])
        
    elif i == 1: 
        point_list.append([num, num + point_list[0][0], True])
    
    elif i == 2:
        if point_list[i-2][0] + num >= point_list[i-1][0] + num:
            point_list.append([num, num + point_list[i-2][0], False])
        # 2 3
        else:
            point_list.append([num, num + point_list[i-1][0], True])
            
    else:
        if point_list[i-1][2] == True:
            if point_list[i-2][1] + num >= point_list[i-3][1] + point_list[i-1][0] + num:
                point_list.append([num, num + point_list[i-2][1], False])
            else:
                point_list.append([num, num + point_list[i-3][1] + point_list[i-1][0], True])
            
        else:
            point_list.append([num, num + point_list[i-1][1], True])

print(point_list[Stairs-1][1])
