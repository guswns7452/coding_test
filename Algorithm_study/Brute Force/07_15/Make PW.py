# Brute Force [암호 만들기]
# https://www.acmicpc.net/problem/1759

# 소요시간 : 23분

import sys
from itertools import combinations
from collections import Counter

L, C = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())

temp_list = list(combinations(arr, L))
all_list = []
for i in temp_list:
    all_list.append(', '.join(sorted(list(i))).replace(', ',''))
    
all_list.sort()
for k in all_list:
    counter = Counter(k)
    sum = 0
    sum += counter["a"]
    sum += counter["e"]
    sum += counter["i"]
    sum += counter["o"]
    sum += counter["u"]
    if sum >= 1 and L - sum >= 2:
        print(k)