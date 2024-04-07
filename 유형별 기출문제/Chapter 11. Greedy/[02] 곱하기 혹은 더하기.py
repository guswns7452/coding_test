## 그리디 문제
## 02 곱하기 혹은 더하기

numList = list(map(int, input()))

sum = 0

for i in numList:
    if sum == 0:
        sum += i
        
    elif not i:
        continue
        
    else:
        sum *= i
            
print(sum)