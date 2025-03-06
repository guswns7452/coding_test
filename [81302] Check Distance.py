# BFS [거리두기 확인하기]
# https://school.programmers.co.kr/learn/courses/30/lessons/81302

# 소요시간 : 51분

# 현재 위치에서 사람들 거리재기
def isSafety(nowPeopleSpot, listPlace):
    start_x, start_y = nowPeopleSpot
    queue = [[start_x, start_y]]
    
    while(queue):
        x, y = queue.pop(0)
        listPlace[x][y] = 0 # 방문한 곳은 0으로 바꿔버림
        
        # 거리가 2까지만 탐색하기
        # O이면 탐색해야할 곳, 거리 2이내 P이면 False를 리턴하여 바로 종료함
        if x+1 < 5 and abs(start_x - (x+1)) + abs(start_y - y) <= 2:
            if listPlace[x+1][y] == 'O':
                queue.append([x+1, y])

            elif listPlace[x+1][y] == 'P':
                return False
        
        if x-1 >= 0 and abs(start_x - (x-1)) + abs(start_y - y) <= 2:
            if listPlace[x-1][y] == 'O':
                queue.append([x-1, y])

            elif listPlace[x-1][y] == 'P':
                return False
            
        if y+1 < 5 and abs(start_x - x) + abs(start_y - (y+1)) <= 2:
            if listPlace[x][y+1] == 'O':
                queue.append([x, y+1])
            
            elif listPlace[x][y+1] == 'P':
                if abs(start_x - x) + abs(start_y - (y+1)) <= 2:
                    return False
            
        if y-1 >= 0 and abs(start_x - x) + abs(start_y - (y-1)) <= 2:
            if listPlace[x][y-1] == 'O':
                queue.append([x, y-1])
        
            elif listPlace[x][y-1] == 'P':
                return False

    # 모두 탐색해도 안전거리를 충족하면 True 리턴
    return True

# 한 대기실에 대한 검증
def searchOnePlace(place):
    listPlace = [] # graph로 입력받음
    people = []    # 사람이 위치해 있는 곳
    for idx, i in enumerate(place):
        listPlace.append(list(i))
        for k in list(filter(lambda x: i[x] == 'P', range(len(i)))):
            people.append([idx, k])
    
    # 모든 사람이 위치해 있는 곳에서 사람간의 거리를 파악해서 안전 거리인지 판단하기
    for nowPeopleSpot in people:
        if not isSafety(nowPeopleSpot, listPlace): 
            return 0
    
    return 1
    

def solution(places):
    answer = []
    for place in places:
        answer.append(searchOnePlace(place))
    return answer