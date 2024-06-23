# HashTable [전화번호 목록]
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 소요시간 : 30분 

#시도 1 
def solution_1(phone_book):
    first = phone_book[0]
    for i in phone_book[1:]:
        if i[0:len(first)] == first:
            print(i[0:len(first)], first)
            return False

    return True

# 시도 2
def solution(phone_book):
    phone_book.sort() # 원소의 길이가 작은 순서대로 정렬 O(NlogN) 
    for idx in range(len(phone_book)-1):
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
            return False
    return True

p = ["119", "97674223", "1195524421"]
print(solution(p))