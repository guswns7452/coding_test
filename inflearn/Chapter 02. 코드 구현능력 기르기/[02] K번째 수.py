# K번째 수

# 테스트 케이스
T = int(input())
AnswerList = []

for i in range(1, T+1):
    N, s, e, k = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    tempList = nums[s-1:e]
    tempList.sort()
    AnswerList.append(tempList[k-1])

for idx, val in enumerate(AnswerList):
    print(f"#{idx+1}", val)
    