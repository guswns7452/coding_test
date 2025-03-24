from collections import deque

T = int(input())

for _ in range(T):
    command = list(input())
    num = int(input())
    listNumber = deque()
    
    if num == 0:
        input()
    elif num == 1:
        listNumber.append(int(input().lstrip('[').rstrip(']')))
    else: 
        listNumber = deque(map(int, input().lstrip('[').rstrip(']').split(',')))

    try:
        for i in command:
            if i == 'R':
                listNumber = deque(reversed(listNumber))
            elif i == 'D':
                listNumber.popleft()
       
        print(str(list(listNumber)).replace(" " , ""))
    
    except:
        print("error")