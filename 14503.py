# 구현 [로봇 청소기]
# https://www.acmicpc.net/problem/14503

# 소요시간 : 72분

# 네 방향에 대해서 갈 수 있으면?
def isGoTofourDirection(N , M, x, y, room, direction):
    goto = {0 : [-1, 0], 1 : [0, 1], 2 : [1, 0], 3 : [0, -1]}
    isAvailable = [] # [방향, 가능/불가능]
    total = 0
    for i in range(direction - 1, (direction - 5), -1):
        if 0 <= x + goto[i%4][0] < N and 0 <= y + goto[i%4][1] < M:
            if room[x + goto[i%4][0]][y + goto[i%4][1]] == 0:
                isAvailable.append([i%4, True])
                total += 1
            else:
                isAvailable.append([i%4, False])

    if total == 0: # 전부 갈 수 없다면
        return False
    return isAvailable # 갈 수 있는 곳이 있다면

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

room = []
answer = 0
for _ in range(N):
    room.append(list(map(int, input().split())))

# 방향 : 북, 동, 남, 서
goto = {0 : [-1, 0], 1 : [0, 1], 2 : [1, 0], 3 : [0, -1]}
status = True
while(status):
    # 현 위치 청소
    if room[x][y] == 0:
        room[x][y] = 2
        answer += 1
    
    # 4칸 중 청소되지 않은 빈칸이 없으면?
    isAvailable = isGoTofourDirection(N, M, x, y, room, direction) # [방향, 가능/불가능]
    if not isAvailable:
        if 0 <= x - goto[direction][0] < N and 0 <= y - goto[direction][1] < M:
            if room[x - goto[direction][0]][y - goto[direction][1]] == 1:
                status = False
            else: x, y = x - goto[direction][0], y - goto[direction][1] # 후진
        else:
            status = False
    # 4칸 중 청소되지 않은 빈칸이 있으면?
    else:
        for k, j in isAvailable:
            if j == True:
                direction = k
                x, y = x + goto[k][0], y + goto[k][1]
                break

print(answer)