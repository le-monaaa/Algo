# baekjoon 24479 깊이 우선 탐색 1 https://www.acmicpc.net/problem/24479

from sys import stdin
input = stdin.readline

def dfs(graph, start):
    global count
    stack = []
    visited = [0 for _ in range(N+1)]
    stack.append(start)
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = count
            count += 1
            stack.extend(reversed(graph[now]))
    return visited

N, M, R = map(int, input().split()) # N: 정점 수 M: 간선 수, R: 시작 정점
arr = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split()) # 양방향 간선
    arr[u].append(v)
    arr[v].append(u)
for n in arr:
    n.sort()
count = 1
visited = dfs(arr, R)

for i in range(1, N+1):
    print(visited[i])