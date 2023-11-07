# baekjoon 1012 https://www.acmicpc.net/problem/1012

from sys import stdin
input = stdin.readline

def is_valid(r, c):
    return 0<=r<M and 0<=c<N
def bfs(sr, sc):
    q = [(sr,sc)]
    table[sr][sc] = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and table[nr][nc] == 1:
                q.append((nr,nc))
                table[nr][nc] = 0

T= int(input()) # tc 수
for tc in range(T):
    M, N, K = map(int, input().split()) # M:가로길이 N:세로길이 K:배추 위치 개수
    table = [[0]*N for _ in range(M)]

    for k in range(K):
        x, y = map(int, input().split())
        table[x][y] = 1

    count = 0
    for r in range(M):
        for c in range(N):
            if table[r][c] == 1:
                bfs(r, c)
                count += 1
    print(count)
