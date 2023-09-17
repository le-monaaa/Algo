# baekjoon 2606 바이러스
# 1번컴퓨터가 웜 바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
# number of computers/num of connections/connections

N = int(input()) # 컴퓨터 수
M = int(input()) # 연결 수
computers = [[] for _ in range (N+1)]
for m in range(M):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

# DFS

stack = []
visited = []

stack.append(1)

while stack:
    node = stack.pop()

    if node not in visited:
        stack.extend(reversed(computers[node]))
        visited.append(node)

print(len(visited)-1)