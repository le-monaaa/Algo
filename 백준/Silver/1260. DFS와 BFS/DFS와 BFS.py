# baekjoon 1260 DFS와 BFS
# DFS로 탐색한 결과 BFS로 탐색한 결과를 출력
# N, M, V/lines // output: DFS result, BFS result

def dfs(graph, start, visited):
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))


def bfs(graph, start, visited):
    q = []
    q.append(start)

    while q:
        node = q.pop(0)

        if node not in visited:
            visited.append(node)
            q.extend(graph[node])



n, m, v = map(int, input().split()) # n:정점개수 m:간선개수 v:탐색시작노드
graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for k in range(n+1):
    graph[k] = sorted(graph[k])

dfs_visited = []
bfs_visited = []

dfs(graph, v, dfs_visited)
bfs(graph, v, bfs_visited)

print(*dfs_visited)
print(*bfs_visited)

