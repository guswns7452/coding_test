## Chapter.4 구현
## 예제 4-1 상하 좌우

## 👍 수행시간 측정 : 4.92057991027832
## 책의 예제 수행시간 측정 : 10.712316989898682

import time

start_time = time.time()
size = int(input())
now = [1,1]
changed = 2

move = list(input().split())

def isOkay():
    if changed == 0:
        if now[1] == 0:
            now[0] += 1
        elif now[1] == size+1:
            now[0] -= 1

    elif changed == 1:
        if now[0] == 0:
            now[0] += 1
        elif now[0] == size+1:
            now[0] -= 1
            
for i in move:
    if i == "R":
        now[1] += 1
        changed = 0
    elif i == "L":
        now[1] -= 1
        changed = 0
        
    elif i == "U":
        now[0] -= 1
        changed = 1
    elif i == "D":
        now[0] += 1
        changed = 1
    
    isOkay()
    
end_time = time.time()
print(now[0],now[1])
print("time : ",end_time-start_time)