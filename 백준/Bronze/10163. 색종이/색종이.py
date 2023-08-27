t = 1001
table = [[0] * t for _ in range(t)]
n = int(input())
i = 1
while i < n+1:
    r1, c1, w, h = map(int, input().split())
    for r in range(r1, r1+w):
        for c in range(c1, c1+h):
            table[r][c] = i

    i += 1
for p in range(1, i+1):
    cnt = 0
    for r in range(t):
        for c in range(t):
            if table[r][c] == p:
                cnt += 1
    if cnt != 0:
        print(cnt)