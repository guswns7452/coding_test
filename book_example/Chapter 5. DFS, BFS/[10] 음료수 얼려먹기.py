## Chapter.5 DFS/BFS
## 예제 5-3 음료수 얼려먹기

## 일단 for문을 돌면서 0인 부분을 찾기
## 찾으면 상하좌우에 대해서 재귀로 DFS 실행 
## 방문했으면 1로 표시
## 재귀를 다 돌고 나오면 결과값에 1 실행
## 다시 반복문 진행


m, n = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input())))
    
def dfs(x,y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(m):
    for j in range(n):
        if dfs(i,j):
            result += 1    

print(result)