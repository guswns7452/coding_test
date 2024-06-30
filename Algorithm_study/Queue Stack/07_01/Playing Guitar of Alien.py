# Queue / Stack [외계인의 기타 연주]
# https://www.acmicpc.net/problem/2841

# 소요시간 : 46분
import sys 

def solution():
    playingList = [[]]
    N, _ = map(int, sys.stdin.readline().split())
    
    for i in range(N):
        playingList.append([])
        
    count = 0
    
    for i in range(N):
        line, pret = map(int, sys.stdin.readline().split())
        prev = playingList[line]
        
        # 손을 떼야 한다면
        while(len(prev) and prev[-1] > pret):
            prev.pop()
            count += 1
        
        # 손을 떼지도 않고, 누를 필요도 없다면?
        if len(prev) and prev[-1] == pret:
            continue
        
        # 손을 눌러야 한다면.
        prev.append(pret) 
        playingList[line] = prev
        count += 1
        
    print(count)
    
solution()