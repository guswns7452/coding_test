# Brute Force [A와 B 2]
# https://www.acmicpc.net/problem/14501

# 소요시간 : 50분

import sys, copy

S = sys.stdin.readline().strip()
T = list(sys.stdin.readline().strip())
S_len = len(S)

def isAvail(S,T):
    global S_len
    
    # 길이가 같아지면 판단
    if S_len == len(T):
        if list(S) == T:
            print(1)
            sys.exit()
    
    # 아니면 계속 줄이는 작업
    else:
        # AAAAB - 더 이상 줄일 수 없음
        if (T[0] == "A" and T[-1] == "B"):
            if list(S) == T:
                print(1)
                sys.exit()
            
        # AAAAA - 뒤의 A를 pop해야함        
        elif (T[0] == "A" and T[-1] == "A"):
            T.pop()
            isAvail(S, T)
        
        # BAAAB - 앞의 B를 pop하고, reverse
        elif (T[0] == "B" and T[-1] == "B"):
            T.pop(0)
            isAvail(S, list(reversed(T)))
        
        # BAAAA - (앞의 B를 pop하고, reverse) or 뒤의 A 해도 됨
        elif (T[0] == "B" and T[-1] == "A"):
            temp = copy.deepcopy(T)
            temp1 = copy.deepcopy(T)

            temp.pop(0)
            isAvail(S, list(reversed(temp)))
            
            temp1.pop()
            isAvail(S, temp1)

isAvail(S, T)
print(0)

