# Graph [단지 번호 붙이기]
# https://www.acmicpc.net/problem/2667

# 소요시간 : 45분

import sys

home = int(sys.stdin.readline())
group = []

def find_first(group):
    for idx, val in enumerate(group):
        for idx_j, val_j in enumerate(val):
            if val_j == '1':
                return (idx, idx_j)
    return (-1,-1)

# 하나의 List로 삽입하는 과정
for i in range(home):
    line = sys.stdin.readline()
    temp_list = []
    for i in range(len(line)-1):
        temp_list.append(line[i])    
    group.append(temp_list)

total_list = []
while(find_first(group) != (-1,-1)):
    temp = find_first(group)    
    stack = list()
    total = list()
    stack.append(temp)
    total.extend(stack)

    while(stack):
        pop_num = stack.pop()
        group[pop_num[0]][pop_num[1]] = 0
        
        # 왼쪽 확인
        if pop_num[1]-1 >= 0 and group[pop_num[0]][pop_num[1]-1] == '1' and (pop_num[0], pop_num[1]-1) not in total:
            stack.append((pop_num[0], pop_num[1]-1))
                
        # 오른쪽 확인
        if pop_num[1]+1 < len(group) and group[pop_num[0]][pop_num[1]+1] == '1' and (pop_num[0], pop_num[1]+1) not in total: 
            stack.append((pop_num[0], pop_num[1]+1))
                
        # 위쪽 확인
        if pop_num[0]-1 >= 0 and group[pop_num[0]-1][pop_num[1]] == '1' and (pop_num[0]-1, pop_num[1]) not in total:
            stack.append((pop_num[0]-1, pop_num[1]))
                
        # 아래쪽 확인
        if pop_num[0]+1 < len(group) and group[pop_num[0]+1][pop_num[1]] == '1' and (pop_num[0]+1, pop_num[1]) not in total:
            stack.append((pop_num[0]+1, pop_num[1]))
        
        total.extend(stack)        

    total_list.append(len(set(total)))
    

total_list.sort()
print(len(total_list))
for i in total_list:
    print(i)