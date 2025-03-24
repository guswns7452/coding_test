import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
sumArr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1, N+1):
        sumArr[i][j] = arr[i-1][j-1] + sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] 

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sumArr[x2][y2] - sumArr[x1-1][y2] - sumArr[x2][y1-1] + sumArr[x1-1][y1-1])
    