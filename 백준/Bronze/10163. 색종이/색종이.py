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
answer = []
for p in range(1, i+1):
    cnt = 0
    for h in table:
        cnt += h.count(p)
    answer.append(cnt)

if answer[-1] == 0:
    for k in answer[:-1]:
        print(k)
else:
    for k in answer:
        print(k)