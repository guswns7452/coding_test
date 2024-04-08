## https://www.acmicpc.net/problem/18406

## 구현 문제. Bronze 2
## ⏰ 권장 소요시간 : 20분
## ⏰ 실제 소요시간 : 6분

point = list(map(int, input()))

point_prev = point[:int(len(point)/2)]
point_after = point[int(len(point)/2):]

if sum(point_prev) == sum(point_after):
    print("LUCKY")
    
else:
    print("READY")