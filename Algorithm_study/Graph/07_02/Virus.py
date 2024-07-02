# Graph [바이러스]
# https://www.acmicpc.net/problem/2606

# 소요시간 : 42분

import sys

com_num = int(sys.stdin.readline())
twin_num = int(sys.stdin.readline())

adj = [ [] for _ in range(com_num+1)]

for _ in range(twin_num):
    src, dest = map(int, sys.stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

stack = list()
total = list()
stack.extend(adj[1])
total.extend(stack)

while(stack):
    now = stack.pop()
    for i in adj[now]:
        if i not in total:
            stack.extend(adj[now])
            total.extend(adj[now])  
        else:
            continue

length = len(set(total))
print(length - 1 if length > 0 else 0)

