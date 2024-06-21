# HashTable [폰켓몬]
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 소요시간 : 10분

# nums = [4,7,8,7,9,5,7,6] (8개)
# 중복 제거한 요소만 추출(set) -> [4,7,8,9,5,6] (6개)
# nums의 절반만 가져갈 수 있으니 nums의 절반 갯수 4개

# Case 1
    # 절반(4개) < 중복 제거한 갯수(6개) = "절반 개수"

# Case 2
    # 절반(4개) > 중복 제거한 갯수(2개) = "중복 제거한 갯수"  

def solution(nums): 
    return len(set(nums)) if len(set(nums)) <= int(len(nums) / 2) else int(len(nums) / 2)

lists = [3,3,3,2,2,2]
print(solution(lists))