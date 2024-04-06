## Chapter.4 구현
## 예제 4-3 왕실의 나이트

## 입력 받은 값을 숫자로 변경함
input_value = list(str(input()))
input_value[0], input_value[1] = ord(input_value[0])-97, ord(input_value[1])-49

step = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
count = 0

for i in step:
    if 0 <= input_value[0] + i[0] <= 7:
        if 0 <= input_value[1] + i[1] <= 7:
            count += 1
            
print(count)