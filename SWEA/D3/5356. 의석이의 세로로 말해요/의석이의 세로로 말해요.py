T = int(input())
for tc in range(1, T+1):
    table = [list(input()) for _ in range(5)]
    n = 0 # table의 최대 길이
    for i in table:
        if len(i) > n:
            n = len(i)
    for i in range(5):
        if len(table[i]) != n:
            for k in range(n-len(table[i])):
                table[i].append("")

    print(f"#{tc}", end= " ")
    for c in range(n):
        for r in range(5):
            if table[r][c]:
                print(table[r][c], end="")
    print()