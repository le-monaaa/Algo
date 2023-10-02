table = []
max_n = 0
rr, cc = 0, 0
for t in range(9):
    table.append(list(map(int, input().split())))

for r in range(9):
    for c in range(9):
        if table[r][c] > max_n:
            max_n = table[r][c]
            rr = r
            cc = c

print(max_n)
print(rr+1, cc+1)