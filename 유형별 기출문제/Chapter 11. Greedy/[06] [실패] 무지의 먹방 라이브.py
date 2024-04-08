# https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

## ⏰ 실제 소요시간 : 58분
## LV.4 무지의 먹방 라이브

## ⛔ 실패
## 효율성은 개차반이였고, 힙으로 풀었던 해설들이 존재했는데,
## 추후 다익스트라를 공부한 후에 다시 풀기로 결정.

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        answer = -1 
    else:
        boolean = True
        while boolean:
            for idx, val in enumerate(food_times):
                if val == 0:
                    continue
                k -= 1
                food_times[idx] -= 1
                if k == 0:
                    boolean = False
                    answer = (idx+1)%len(food_times) +1
                    break
    return answer            

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))