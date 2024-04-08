## ⏰ 권장 소요시간 : 30분
## ⏰ 실제 소요시간 : 18분

## 무게가 각기 다른 볼링공의 조합의 갯수

## ⌨️ 입력 : 볼링공 갯수 n개, 볼링공 무게 m개
## ⌨️ 입력 : 볼링공 리스트들 n개의 입력

# ✅ 풀이방법
## [처음] 처음에는, 무게마다 리스트를 만들려했다. weight[1] = 2 // 무게가 1인 공이 2개임
## 이렇게 하면, 조합에 중복이 생긴다.

## [현재] 순서를 따지지 않는 set에 tuple로 생성하였다.
## 조합에 문제가 생길까 했는데, 반복문이 이전에 공들은 고려하지 않아 중복이 생기지 않았다.

n, m = map(int, input().split())

boling = list(map(int, input().split()))

sets = set()

for idx, val in enumerate(boling):
    for j in range(idx+1, n):
        if val != boling[j]:
            sets.add(tuple([idx, j]))

print(len(sets))