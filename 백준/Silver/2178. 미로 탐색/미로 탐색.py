# baekjoon 2178 미로 탐색
# 1,1에서 N,M으로 도착할 때의 최소 칸 수
# N, M/ n lines M values

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = []
for n in range(N):
    maze.append(list(map(int, list(input()))))

# BFS

q = []
visited = []
q.append((0,0))
visited.append((0,0))
move = 0

while q:
    size = len(q)
    for _ in range(size):
        r, c = q.pop(0)

        if (r, c) == (N-1, M-1):
            q = []
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in visited and maze[nr][nc] != 0:
                q.append((nr,nc))
                visited.append((nr,nc))

    move += 1

print(move)