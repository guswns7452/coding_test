## n행과 m열
n, m = map(int, input().split())

numList = []
minimal = 0

## 배열 입력 받기
for _ in range(n):
    numList.append(list(map(int, input().split())))

## 최솟값 찾기.
for i in numList:
    if minimal < min(i):
        minimal = min(i)
        
print(minimal)