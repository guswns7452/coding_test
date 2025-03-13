# 구현 [토마토]
# https://www.acmicpc.net/problem/759

# 소요시간 : 35분

import copy
M, N, H = map(int, input().split())
answer = 0

graph = [[] for _ in range(H)]

for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

queue = []

# 6방향
direction = [[1, 0 ,0], [-1, 0, 0], [0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0]]

for z in range(H):
    for y, value in enumerate(graph[z]):
        for x, value_x in enumerate(value):
            if value_x == 1:
                queue.append([z, y, x])

sub = []
while(queue):
    now = queue.pop()

    # 6방향
    for z, y, x in direction:
        if 0 <= z + now[0] < H and 0 <= y + now[1] < N and 0 <= x + now[2] < M and graph[now[0] + z][now[1] + y][now[2] + x] == 0:
            sub.append([z + now[0], y + now[1], x + now[2]])
            graph[now[0] + z][now[1] + y][now[2] + x] = 1

    if not len(queue):
        answer += 1
        queue = copy.deepcopy(sub)
        sub = []

for z in range(H):
    for value in graph[z]:
        if 0 in value:
            print(-1)
            exit()


print(answer-1)
        
