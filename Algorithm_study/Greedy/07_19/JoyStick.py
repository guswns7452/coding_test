# Greedy [조이스틱]
# https://school.programmers.co.kr/learn/courses/30/lessons/42860

# 소요시간 : 105분

# ============== 폐기 ================== #

# index 1에 A 1개가 있으면 뒤로 돌아가는게 좋음 "JABBBB"
# index 2에 A 2개가 있으면 뒤로 돌아가는게 좋음 "JKAABB" -> 4
# index 3에 A 3개가 있으면 뒤로 돌아가는게 좋음 "JKAAAB" -> 4
# index 3에 A 2개가 있고, 맨뒤에 A이면 앞으로 가는게 좋음 "JKAABA" -> 4

# 앞의 A는 index와 관계가 있음
# 맨 뒤의 A는 앞의 A의 갯수와 관계가 있음

# A의 범위가 1개이고, index 갯수와 연관이면 역방향
# A의 범위가 2개 이상
    # A가 맨 뒤에 있을 경우
        # 맨 앞 A가 index 갯수보다 많고, 맨 앞 A가 맨 뒤 A보다 3개 이상 역방향 
        # 맨 앞 A가 index 갯수보다 2개 더 많고, 맨 앞 A가 맨 뒤 A보다 3개 이상 역방향 
        # 맨 앞 A가 index 갯수보다 많고, 맨 앞 A가 맨 뒤 A보다 2개 이하 정방향 
        # 그렇지 않으면 정방향 
    # A가 맨 뒤에 없을 경우
        # 정방향이 좋음

# BAAABBBAAABBBAAABBB -> 역방향 좋음
# BAAABBBAAABBBAAA -> 상관없음 (정방향?)
# BABBBAAABBBAA -> 정방향
# BABBBAAABBBAAAB -> 역방향
# BAAABBBAAABBBAA -> 정방향
# BBBAAAAABBBAAAA -> 역방향
# BAAAAABBBAAABBB -> 역방향
# KAAAAAAAAAAAAAAK -> 역방향
# BBBBBBBBABA -> 정방향
# BBBBAAABA -> 정방향
# 5-8 / 11-12
# 계속 A가 다 맞는지 체크?

# ======================================== #

# 그냥 정방향 역방향 비교하자..
# A 만나면 역방향 가는거랑, 그냥 정방향 때리는거랑.
# BAAAAAAAAAAAAABABAB
# A : 65 / (13번) N : 78 (13번) / Z : 90
def solution(name):
    list_name = list(name)
    list_str = ['A'] * len(list_name)

    # 냅다 정방향
    count = 0
    for idx, i in enumerate(list_name):
        if ord(i) > 78:
            count += 90-ord(i) + 1
        else:
            count += ord(i) - 65
        list_str[idx] = i
        if list_str == list_name:
            break
        count += 1
        
    # 2 : 정방향 -> 역방향
    count_recv = 0
    list_str = ['A'] * len(list_name)
    # 정방향으로 탐색하다가
    for idx, j in enumerate(list_name):
        if ord(j) > 78:
            count_recv += 90-ord(j) + 1
        else:
            count_recv += ord(j) - 65
        list_str[idx] = j
        
        if idx != len(list_name)-1 and list_name[idx+1] == 'A':
            count_recv += idx + 1
            break
        count_recv += 1

    # A를 만나면 역방향
    length = len(list_name)
    for idx, j in enumerate(list(reversed(list_name))):  
        if ord(j) > 78:
            count_recv += 90-ord(j) + 1
        else:
            count_recv += ord(j) - 65
        list_str[length-idx-1] = j
        if list_str == list_name:
            break
        count_recv += 1
    
    # 3 : 역방향 -> 정방향
    count_recv_2 = 1
    list_str = ['A'] * len(list_name)
    length = len(list_name)
    for idx, j in enumerate(list(reversed(list_name))):  
        if ord(j) > 78:
            count_recv_2 += 90-ord(j) + 1
        else:
            count_recv_2 += ord(j) - 65
        list_str[length-idx-1] = j
        if j != "A" and list_name[length-idx-2] == 'A':
            count_recv_2 += idx + 1
            break
        count_recv_2 += 1
    
    for idx, j in enumerate(list_name):
        if ord(j) > 78:
            count_recv_2 += 90-ord(j) + 1
        else:
            count_recv_2 += ord(j) - 65
        list_str[idx] = j
        
        if list_str == list_name:
            break
        count_recv_2 += 1
            
    # 역방향
    count_recv_3 = 1
    list_str = ['A'] * len(list_name)
    length = len(list_name)
    for idx, j in enumerate(list(reversed(list_name))):  
        if ord(j) > 78:
            count_recv_3 += 90-ord(j) + 1
        else:
            count_recv_3 += ord(j) - 65
        list_str[length-idx-1] = j
        if list_str == list_name:
            break
        count_recv_3 += 1
    return min(count, count_recv, count_recv_2, count_recv_3)
    
name = "BAAAAAABAAAABABABAB"
print(solution(name))