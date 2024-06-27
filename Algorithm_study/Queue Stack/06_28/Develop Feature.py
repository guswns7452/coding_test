# Queue / Stack [기능개발]
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 소요시간 : 20분

def solution(progresses, speeds):
    answer = []
    while(progresses):
        # 하룻 밤 덧셈 연산
        for idx, (val_p, val_s)  in enumerate(zip(progresses, speeds)):
            progresses[idx] = val_p + val_s
        
        # 판단하는 코드
        for idx, _  in enumerate(zip(progresses, speeds)):
            # 100을 넘긴 요소를 찾아냄
            if idx == 0 and progresses[idx] >= 100:
                count = 0
                
                # 만약 100을 넘겼다면, count += 1, 아니면 break
                for idx, val in enumerate(progresses):
                    if val >= 100:
                        count += 1
                    else: 
                        break
                
                # 100을 넘긴 요소 pop 함
                for i in range(count):
                    speeds.pop(0)
                    progresses.pop(0)
                answer.append(count)
                
    return answer

progresses = [99, 96, 94]
speeds = [1, 3, 4]
print(solution(progresses, speeds))