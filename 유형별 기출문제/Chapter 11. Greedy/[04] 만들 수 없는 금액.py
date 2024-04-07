## ⏰ 권장 소요시간 : 30분
## ⏰ 실제 소요시간 : 38분

## 동전을 가지고 만들 수 없는 금액을 찾아라.

## ⌨️ 입력 : 동전 6개
## ⌨️ 입력 : 3,2,5,1,1,7 -> 동전의 단위

## 풀이방법
### 1. 바로 그 동전이 존재하는 경우 ✅ 
### 2. 더 이상 값이 없을 때. 총합을 넘길 때 ✅ 
### 3. 구해야 할 값보다 작은 값을 가진 리스트로 나눔
#### 3-1. 제일 큰 값에서 빼고, 리스트를 또 나눈 다음 재귀 호출 반복

m = int(input())

coin = list(map(int, input().split()))
coin.sort()

boolean = True

def isCoin(target, subList):
    global boolean
    temp = target - subList[-1]
    subList.pop(-1)
    
    if temp in coin:
        boolean = True
        return
    
    newList  = [x for x in subList if x < temp]
    
    if sum(newList) < temp:
        boolean = False
        return
    
    if temp == 0:
        boolean = True
        return
        
    else:
        isCoin(temp, newList)
    

i = 0
while True:
    i += 1
    if i in coin:
        continue
    elif i >= sum(coin): ## 최대에 도달했을 때
        break
    else:
        newList  = [x for x in coin if x < i]
        isCoin(i, newList)
        if boolean == False:
            break
        
print(i)
        