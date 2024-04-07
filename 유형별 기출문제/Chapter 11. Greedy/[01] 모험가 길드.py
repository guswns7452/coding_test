## 그리디 문제
## 01 모험가 길드

## 📢 문제 : 공포도가 N인 사람은 무조건 N명 이상의 그룹으로 조합

## ⌨️ 입력 : 모험가 수 N
## ⌨️ 입력 : 모험가들의 공포도 값
## 🖥️ 출력 : 최대 그룹 수

n = int(input())
members = list(map(int, input().split()))
members.sort()

count = 0  # 현재 그룹의 멤버 수
result = 0
for i in members:
    count += 1
    if count >= i: # 공포도와 같거나 커지면, 그룹 형성
        result += 1
        count = 0
    
print(result)