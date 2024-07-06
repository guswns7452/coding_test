## 오름 차순으로 선택 정렬
def select_sort(list):
    for i,v in enumerate(list):
        min = v
        min_index = i
        # 최솟 값 찾기
        for j in range(i, len(list)):
            if list[j] < min:
                min = list[j]
                min_index = j
        
        list[i], list[min_index] = min, list[i] 
            
    print(list)

def Insertion_sort(list):
    sortedList = []
    sortedList.append(list.pop(0))
    len_list = len(list)
    for _ in range(len_list):
        now = list.pop(0)
        print(f"{sortedList} |   {now}   | {list}")
        now_index = 0
        
        for j, v_j in enumerate(sortedList):
            if v_j <= now:
                now_index = j + 1
                
        sortedList.insert(now_index, now)

def bubble_sort(list):
    for i in range(len(list)-1):
        print(f"{i+1} : {list}") 
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    # SubList 2개로 나누는 과정
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

list = [7,5,9,5,49,38,4,5,2,3]           
print(merge_sort(list))