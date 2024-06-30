# Queue / Stack [다리를 지나는 트럭]
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 소요시간 : 55분

def solution(bridge_length, weight, truck_weights):
    list = []
    count = []
    for i in range(1, 10001):
        try:
            if sum(list) + truck_weights[0] <= weight:
                list.append(truck_weights.pop(0))
                count.append(bridge_length)
            
            for idx, val in enumerate(count):
                count[idx] -= 1
                
            for idx, val in enumerate(count):
                if val == 0:
                    count.pop(0)
                    list.pop(0)
                    if (len(truck_weights) == 0 and len(list) == 0):
                        if bridge_length == 1:
                            return i+1
                        return i
                        
                else:
                    break
        except IndexError:
            return i+count[-1]
        
bridge_length = 3
weight = 1
truck_weights = 	[1, 1, 1]
print(solution(bridge_length, weight, truck_weights))