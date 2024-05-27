# 4. 대표 값

n = int(input())
numList = list(map(int, input().split()))

sortedNum = sorted(numList)

avg = round(sum(numList)/len(numList))
diff = [i-avg for i in sortedNum]
print(avg, end=" ")

l = [abs(x) for x in diff]

if min(l)+avg in numList:
    print(numList.index(min(l)+avg)+1)

else: 
    print(numList.index(avg-min(l))+1)