# SWEA 1861 정사각형 방
# N^2개의 방, 각각의 방의 번호가 유니크할 때, 이동하려는 방의 숫자는 현재 방보다 1 커야만 함.
# 어느 방에서 출발해여 가장 많은 수의 방을 탐색할 수 있는지
# T/ N/ N lines N values
# 처음에 출발해야 하는 방 번호, 이동 가능한 방 개수

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())
for tc in range(1, T+1):
    n = int(input()) # n: 방의 갯수/n
    rooms = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = 0
    max_start = 1000

    for r in range(n):
        for c in range(n):
            i, j = r, c
            cnt = 1
            while True:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0<= nr < n and 0<= nc< n and rooms[nr][nc] == rooms[r][c] +1:
                        r, c = nr, nc
                        cnt += 1
                        break
                else:
                    break # 갈 곳이 없으면 종료,
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_start = rooms[i][j]
                elif max_cnt == cnt and max_start > rooms[i][j]:
                    max_start = rooms[i][j]

    print(f"#{tc} {max_start} {max_cnt}")