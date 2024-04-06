## Chapter.4 구현
## 예제 4-2 시각

## 책에서는 삼중 for문으로 +1하면서 체크했으나, 3이 나오는 모든 경우를 계산한 코드

# 00:00:00 ~ 0N:59:59 까지 3이 나오는 횟수 세기

hour = 0
min = 0
sec = 0

sum = 0
input_hour = int(input())

## 0 ~ 60까지 3이 나오는 횟수 15번
for i in range(input_hour+1):
    if i == 3:
        sum += 60 ** 2
    else:
        sum += (15 * 60) + (15 * 45)
        
print(sum)