# baekjoon 24445 

from collections import deque

from sys import stdin
input = stdin.readline
def bfs(graph, start):
    count = 1
    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(N+1)]

    while queue:
        now = queue.popleft()
        if not visited[now]:
            visited[now] = count
            count += 1
            queue.extend(graph[now])
    return visited

N, M, R = map(int, input().split()) # N:정점수 M:간선수 R:시작정점
arr = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split()) # 양방향
    arr[u].append(v)
    arr[v].append(u)
for ar in arr:
    ar.sort(reverse=True)
result = bfs(arr, R)

for i in range(1, N+1):
    print(result[i])
