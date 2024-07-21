# Greedy [큰 수 만들기]
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# ⏰ 소요시간 : 65분

def solution(number, k):
    answer = []

    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

number = "438769"
k = 3
print(solution(number, k))