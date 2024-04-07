# https://www.acmicpc.net/problem/1439

## 구간을 나누고, 나뉜 갯수의 절반 만큼이 뒤집을 개수

numList = list(input())

subList = []
splitList = []

count = 0
now = 2

for num in numList:
    i = int(num)
    if now != i:
        subList.append(splitList)
        splitList = []
        now = i
    
    splitList.append(i)

subList.append(splitList)
subList.pop(0)

## 구간의 개수중에서 절반만 뒤집으면 됨
print(int(len(subList)/2))