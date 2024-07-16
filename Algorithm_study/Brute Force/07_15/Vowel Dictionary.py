# Brute Force [모음 사전]
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 소요시간 : 12분

from itertools import product

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', "U"]
    dict = []
    
    # 한개인 경우부터 다섯개인 경우까지
    list_ = list(product(vowels))
    list_.append(list(product(vowels, vowels)))
    list_.append(list(product(vowels, vowels, vowels)))
    list_.append(list(product(vowels, vowels, vowels, vowels )))
    list_.append(list(product(vowels, vowels, vowels, vowels, vowels )))
    
    # Set을 String으로 바꿈
    for s in list_:
        for k in s:
            S = ', '.join(k).replace(', ','')
            dict.append(S)
    dict.sort() # 순서 정렬
    return dict.index(word) + 1

print(solution("AAAE"))