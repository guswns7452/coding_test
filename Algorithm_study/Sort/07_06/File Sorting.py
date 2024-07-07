# Sort [[3차] 파일명 정렬]
# https://school.programmers.co.kr/learn/courses/30/lessons/17686

# 소요시간 : 29분

# 1. 파일 명 List
# 2. 문자 / 숫자 / Tail / 기존 문자열 -> List
# 3. 비교

def solution(files):
    answer = []
    new_file_list = []
    for i in files:
        start_index, end_index = 0, 0
        for idx_j, j in enumerate(i):
            # Ascii
            if ord(j) <= 57 and 48 <= ord(j): 
                if start_index == 0:
                    start_index = idx_j
                    end_index = idx_j + 1
                else:
                    end_index = idx_j + 1
            # index 다 알아냈으면 break
            elif start_index != 0 and end_index != 0:
                break
        new_file_list.append([i, i[:start_index].lower(), i[start_index:end_index], i[end_index:]])
    
    ## [문자열 정렬] 입력 순서가 바뀌면 안되니, Bubble Sort 
    for idx, _ in enumerate(new_file_list):
        for idx_j in range(len(new_file_list)-idx-1):
            if new_file_list[idx_j][1] > new_file_list[idx_j+1][1]:
                new_file_list[idx_j], new_file_list[idx_j+1] = new_file_list[idx_j+1], new_file_list[idx_j]
            
            ## [문자열이 같으면 숫자 정렬] 입력 순서가 바뀌면 안되니, Bubble Sort 
            elif new_file_list[idx_j][1] == new_file_list[idx_j+1][1] and int(new_file_list[idx_j][2]) > int(new_file_list[idx_j+1][2]):
                new_file_list[idx_j], new_file_list[idx_j+1] = new_file_list[idx_j+1], new_file_list[idx_j]

    # 정렬된 값 중 파일명만 모음
    for i in new_file_list:
        answer.append(i[0])           
    
    print(answer)            
    return answer

files =["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))