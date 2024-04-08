# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

## 구현 문제 : 문자열 압축
## ✨ 난이도 1.5/3

## ⏰ 권장 소요시간 : 30분
## ⏰ 실제 소요시간 : 28분

def solution(s):
    s = list(s)
    answer = 0
    lower = 1001
    
    for i in range(1,len(s)+1):
        copy_s = s.copy()
        makedString = ""
        now = 0
        count = 0
        
        while len(copy_s):
            n = ''
            
            ## 횟수를 늘려가며, 겹치는 패턴 찾기
            ## 중간에 IndexError가 발생하면, 문자열을 모두 빼냈다는 이야기
            for j in range(i):
                try:
                    n += copy_s.pop(0)
                except:
                    break
            
            ## 처음이면, 현재 문자 세팅하기
            if count == 0:
                now = n
            
            if n != now and count != 0:
                if count == 1:
                    makedString += now
                else:
                    makedString += (str(count) + now)
                count = 1
                now = n
            else:
                count += 1
        
        ## 뒤에 남은 문자열 붙이기    
        if count == 1:
            makedString += now
        else:
            makedString += (str(count) + now)
            
        if lower > len(makedString):
            lower = len(makedString)
    
    answer = lower
    return answer

string = input()
print(solution(string))