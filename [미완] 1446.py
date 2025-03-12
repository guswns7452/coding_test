import sys

N, D = map(int, sys.stdin.readline().split())
route = []
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end > D: ## 지름길이 범위를 넘는건 빼기
        continue
    route.append([start, end, length])
    
route.sort(key=lambda x: x[0])

print(route)



for idx, value in enumerate(route):
    for i in route[idx:]:
        


# 0, 10, 9 -> 0, 10 / 1
# 50, 70, 15 -> 0, 70 / 6
# 140, 160, 14 -> 0, 160 / 12
# 160, 180, 14 -> 0, 180 / 18

# 80, 190, 100 -> 0, 190 / 16

