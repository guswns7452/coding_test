from itertools import combinations

# 입력 받기
N, k = map(int, input().split())
num = list(map(int, input().split()))

# 중복 제거 및 정렬 (내림차순)
num = sorted(set(num), reverse=True)

# 모든 3개 숫자의 조합을 계산하고 합산
sums = [sum(combo) for combo in combinations(num, 3)]

# 중복된 합산 값 제거 및 정렬 (내림차순)
sums = sorted(set(sums), reverse=True)

# k번째로 큰 값을 출력 (0-based index이므로 k-1)
print(sums[k-1])