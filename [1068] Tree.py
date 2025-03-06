# Graph [트리]
# https://www.acmicpc.net/problem/1068

# 소요시간 : 34분


# 입력으로 무시
length = int(input())

# 연결 한번에 입력받기
list_graph = list(map(int, input().split()))
graph = [[] for _ in range(length)]

# graph 연결 만들기
for idx, i in enumerate(list_graph):
    if i >= 0: 
        graph[i].append(idx)
    
# 삭제한 노드 번호
delete_num = int(input())
queue = [delete_num]

# 부모 노드에서 연결 삭제
delete_parent = list_graph[delete_num]
try:
    graph[delete_parent].remove(delete_num)
except ValueError:
    pass

# 자식 노드에서 연결 삭제
while(queue):
    last_idx = queue.pop(0)
    if len(graph[last_idx]) > 0:
        queue += graph[last_idx]
    
    graph[last_idx] = -1

print(graph.count([]))
    

print(dir(list))
