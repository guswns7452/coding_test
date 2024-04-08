## ⏰ 권장 소요시간 : 20분
## ⏰ 실제 소요시간 : 10분

inputs = list(input())
inputs.sort()

sum = 0

while True:
    if 65 <= ord(inputs[0]) and ord(inputs[0]) <= 90:
        break
    else:
        sum += int(inputs.pop(0))
        
for i in inputs:
    print(i,end='')
    
print(sum)