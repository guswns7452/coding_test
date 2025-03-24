N, K = map(int, input().split())
graph = list(input())

hamberger = []
person = []
answer = 0

for idx, i in enumerate(graph):
    if i == 'P':
        isTrue = True
        for j in range(K, 0, -1):
            if 0 <= idx-j < len(graph) and graph[idx-j] == 'H':
                graph[idx-j] = 0
                answer += 1
                isTrue = False
                break
    
        if isTrue:
            for j in range(1, K+1):
                if 0 <= idx+j < len(graph) and graph[idx+j] == 'H':
                    graph[idx+j] = 0
                    answer += 1
                    break

print(answer)