# Brute Force [리모컨]
# https://www.acmicpc.net/problem/1107

# 소요시간 : 실패

import sys

goto = int(sys.stdin.readline())
goto_list = list(map(int, str(goto)))
    
N = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))

# [1,1,1,1,0,1,1,1,1,0]
avail = [] # 사용 가능한 버튼 1 / 사용 불가 0
for i in range(10):
    if i in broken:
        avail.append(0)
    else:
        avail.append(1)

# 4 9
## 99999
## 100000
## 38888

min_avail = avail.index(1)
if min_avail == -1: # 모든 버튼 이용 불가시
    print(abs(goto-100))
    sys.exit()    
reversed_avail = list(reversed(avail))
max_avail = abs(reversed_avail.index(1)-len(goto_list)+1)

attemp = [abs(goto-100)]

now = 0
unavil = -1
for idx, val in enumerate(goto_list):
    now *= 10
    if avail[val] == 0:
        unavil = idx
    else:
        now += val 

top = now
bottom = now

# 어딘가 중간에 누르지 못함
if unavil != -1:
    # 965 - 600 : 위 번호를 누르는게 빠를까?
    for k in range(goto_list[unavil],10):
        if avail[k] == 1:
            top += k
            break
    
    # 위 번호를 누를 버튼이 없으면?
    if top == now:
        for k in range(top%10, 10):
            if avail[k] == 1:
                top /= 10
                top *= 10
                top += k
                break
        if top == now:
            pass
        top += min_avail
    
    for _ in range(unavil+1, len(goto_list)+1):
        top *= 10    
        top += min_avail
    
    attemp.append(len(str(top))+abs(top-goto))

    # 998 - 997            
    # 500 - 499 : 아래 번호를 누르는게 빠를까?
    for t in range(val-1,-1,-1):
        if avail[k] == 1:
            bottom += k
            break
    
    for _ in range(unavil+1,len(goto_list)+1):
        bottom *= 10
        bottom += min_avail
        print(bottom)
        attemp.append(len(str(bottom))+abs(bottom-goto))
        
# 100번에서 + - 하는 것 / 번호 눌러서 근처까지가서 + - 하는 거 [비교]
print(attemp)        
print(min(attemp))
