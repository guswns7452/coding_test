# Sort [알고리즘 수업 - 삽입 정렬 3]
# https://www.acmicpc.net/problem/24053

# 소요시간 : 5분 

import sys

input = sys.stdin.read # 한 번에 모든 내용 입력받음
data = input().split() # 공백 기준으로 분리

A = int(data[0])
arr = list(map(int, data[1:A+1]))
comp_arr = list(map(int, data[A+1:]))

def insertion_sort(arr):
    isSame = False
    for i in range(1, A): # 기준 idx와 idx-1을 비교하여 정렬해야 하므로 idx 1부터 시작
        key = arr[i]  # 정렬된 부분에 삽입될 값
        j = i - 1 # key를 알맞은 위치에 삽입하기 위해 비교할 인덱스 j 설정

        # 정렬된 부분(arr[0:i-1])에서 key보다 큰 값 뒤로 한 칸씩 이동
        while j >=  0 and arr[j] > key: 
            arr[j + 1] = arr[j]
            j -= 1
            if comp_arr == arr:
                print(1)
                return
    
        if j + 1 != i: # key가 삽입되는 경우
            arr[j + 1] = key # key를 적절한 위치에 삽입
            if comp_arr == arr:
                print(1)
                return
            
    if isSame == False:
        print(0)
        return        
    

insertion_sort(arr)