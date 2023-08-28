T = int(input())
for tc in  range(1, T+1):
    n = int(input()) # 농장의 크기
    farm = [list(map(int, input())) for _ in range(n)]
    middle = n//2
    sum = 0
    for r in range(n):
        for c in range(n):
            if abs(r - middle) + abs(c - middle) <= middle:
                sum += farm[r][c]

    print(f"#{tc} {sum}") 