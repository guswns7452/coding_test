# DP [1,2,3 더하기]
# https://www.acmicpc.net/problem/9095

# ⏰ 소요시간 : 40분

import sys, copy

T = int(sys.stdin.readline())
nums = []

for _ in range(T):
    nums.append(int(sys.stdin.readline()))
max_nums = max(nums)

all_count = [0 for _ in range(max_nums + 1)]
all_count[1] = 1
all_count[2] = 2
all_count[3] = 4

one_prev = [[1,1,1],[1,2],[2,1],[3]]
two_prev = [[1,1],[2]]
three_prev = [[1]]

def insert_num(now_list, num, i):
    # 모든 구간에 1 삽입함
    for idx in range(len(i)+1):
        temp_list = copy.deepcopy(i)
        temp_list.insert(idx, num)
            
        if temp_list not in now_list:
            now_list.append(temp_list)

    return now_list

for j in range(4, max_nums + 1):
    now_list = []
    for i in one_prev:
        now_list = insert_num(now_list, 1, i)
            
    for i in two_prev:
        now_list = insert_num(now_list, 2, i)
            
    for i in three_prev:
        now_list = insert_num(now_list, 3, i)
        
    all_count[j] = len(now_list)
    three_prev = copy.deepcopy(two_prev)
    two_prev = copy.deepcopy(one_prev)
    one_prev = copy.deepcopy(now_list)
    
for k in nums:
    print(all_count[k])
    
