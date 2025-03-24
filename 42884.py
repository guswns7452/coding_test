# Greedy [단속카메라]
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

# 소요시간 : 분

import copy
# 3시 10분에 시작함
def solution(routes):
    answer = 0
    spot = [0 for _ in range(60002)]
    
    for route in routes:
        x, y = route
        for i in range(x + 30000, y + 30000 + 1):
            spot[i] += 1
        
    routes.sort(key=lambda x : x[0])
    startIndex = routes[0][0] + 30000
    endIndex = routes[-1][1] + 30000
    
    while(routes):
        findedIndex = spot[startIndex:endIndex+1].index(max(spot[startIndex:endIndex+1])) + startIndex
        temp_routes = copy.deepcopy(routes)
        for idx, i in enumerate(temp_routes):
            if i[0] + 30000 <= findedIndex <= i[1] + 30000:
                routes.remove(i)
            else:
                startIndex = temp_routes[idx+1][0] + 30000
                break

        answer += 1
    return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

def solution2(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    print(routes)
    for route in routes:
        print(camera)
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


print(solution2([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))