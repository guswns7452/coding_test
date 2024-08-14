# DFS [단어 변환]
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

# ⏰ 소요시간 : 14분

from collections import deque

def appendable(now_word, words):
    appendable_words = []
    # 두 문자열의 각 문자 비교
    for word in words:
        diff_count = 0
        for char1, char2 in zip(now_word, word):
            if char1 != char2:
                diff_count += 1
                if diff_count > 1:
                    break
        if diff_count == 1:
            appendable_words.append(word)
    return appendable_words
    
def solution(begin, target, words):
    # target이 없으면 
    if target not in words:
        return 0

    answer = 0
    visited = dict()
    visited[begin] = False
    for i in words:
        visited[i] = False
        
    stack = deque()
    stack.append([begin, 0])
        
    while(stack):
        now_word, count = stack.pop()
        
        # 타켓 단어라면 정답 갱신
        if now_word == target:
            if answer == 0:
                answer = count
            elif answer > count:
                answer = count
        
        # 단어 하나씩 다른 것들을 계속해서 추가함. 
        if visited[now_word] == False:
            visited[now_word] = True
            for word in appendable(now_word, words):
                if visited[word] == False:
                    stack.append([word, count+1])
    
    return answer