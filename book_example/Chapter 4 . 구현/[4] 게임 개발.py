## Chapter.4 구현
## 예제 4-3 왕실의 나이트

n, m = map(int, input().split())

now = list(map(int, input().split()))
direction = now.pop()
directionToGo = {0 : [-1,0], 1 : [0,1], 2 : [1,0], 3 : [0,-1]}
maps = []
count = 1
roundCount = 0

## 갈 수 있는지 판단하는 코드
def isAvailable(goto):
    global direction, now, roundCount,count
    dx,dy = now[0]+goto[0], now[1]+goto[1]
    
    ## 갈 수 있다면 이동
    if maps[dx][dy] == 0:
        maps[now[0]][now[1]] = 2
        roundCount = 0
        now = [dx, dy]
        count += 1
    
    ## 갈 수 없으면 방향 변경
    else:
        roundCount += 1
        direction -= 1
        direction %= 4
        if(direction < 0): direction += 4
        
        ## 방향 회전을 다 했는데도 갈 곳이 없으면 뒤로 가기.
        if roundCount == 4:
            maps[now[0]][now[1]] = 2
            roundCount = 0
            goto = directionToGo.get(direction)
            now = [now[0]-goto[0], now[1]-goto[1]]
            if maps[now[0]][now[1]] == 1:
                return False 

for _ in range(m):
    maps.append(list(map(int, input().split())))

while True:
    goto = directionToGo.get(direction)
    status = isAvailable(goto)
    if status == False:
        break

print(count)