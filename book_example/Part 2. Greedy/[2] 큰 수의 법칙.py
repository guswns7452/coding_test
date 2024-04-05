## Part 2. Greedy
## p.92 큰 수의 법칙

### 입력 : 배열의 크기 N, M번의 덧셈, K번을 초과하여 더해질 수 없음
### 입력 : 배열 [5,2,5,4,6]


## 배열의 크기, 더해야하는 수, 초과하여 더할 수 없는 수
size, addingCount, notOverAdd = map(int, input().split())
sum = 0

numList = list(map(int, input().split()))

## 배열 sort하기.
numList.sort()

## 반복문
for i in range(addingCount):
    if not ((i+1)%notOverAdd):
        sum += numList[-2]
        continue
    sum += numList[-1] 

print(sum)