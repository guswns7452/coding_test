# https://school.programmers.co.kr/learn/courses/30/lessons/60059?language=python3

## 구현 문제 : 자물쇠와 열쇠
## ✨ 난이도 1.5/3

## ⏰ 권장 소요시간 : 40분
## ⏰ 실제 소요시간 : 147분... [실패]

import copy

def solution(key, lock):
    answer = True
    answer = False
    
    if lock == [[1] * (len(lock)) for _ in range(len(lock))]:
        return True
    
    def rotate(key):
        copy_key = []
        copy_key = copy.deepcopy(key)
        for i in range(3):
            for j in range(3):
                # print(copy_key[abs(j-2)][i], " ", abs(j-2))
                key[i][j] = copy_key[abs(j - 2)][i]

    def prints(list):
        for i in list:
            print(i)        
        print()
        
    # lock의 3배 크기의 배열에 중앙에 위치시킴.
    copys = [[0] * (len(lock)*3) for _ in range(len(lock)*3)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            copys[len(lock)+i][len(lock)+j] = lock[i][j]
        
    
    ## 중앙이 모두 1인지 체크하는 함수
    def isOne(list):
        copyList = list[len(lock):len(lock)*2]
        for i in copyList:
            if i[len(lock):len(lock)*2] != [1] * len(lock):
                return False
            
        return True

    
    for o in range(4):
        rotate(key)
        for i in range(len(copys)-len(key)+1):
            if answer: break
            for j in range(len(copys)-len(key)+1):
                if answer: break
                deepCopy = copy.deepcopy(copys)
                for k in range(len(key)):
                    for p in range(len(key)):
                        deepCopy[i+k][j+p] += key[k][p] 
                if isOne(deepCopy) == True:
                    answer = True
        
    return answer


key, lock = [], []
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# for i in range(3):
# 	key[i] = list(map(int, input().split()))
#
# for i in range(3):
# 	lock[i] = list(map(int, input().split()))

print(solution(key, lock))
