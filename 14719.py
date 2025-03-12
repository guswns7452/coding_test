# 구현 [빗물]
# https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
graphic = [[0 for _ in range(H)] for _ in range(W)]

inputList = map(int, input().split())

for idx, j in enumerate(inputList):
    for k in range(j):
        graphic[idx][k] = 1

transposed = list(map(list, zip(*graphic)))
total = 0
for i in transposed:
    startPoint = -1
    for idx, j in enumerate(i):
        if j == 1:
            if startPoint != -1 and idx - startPoint != 1:
                total += (idx - startPoint - 1) 
            startPoint = idx
            
print(total)