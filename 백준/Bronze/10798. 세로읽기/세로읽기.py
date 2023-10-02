table = []
length = 0

for i in range(5):
    table.append(list(input()))
    if length < len(table[i]):
        length = len(table[i])

for i in range(5):
    if len(table[i]) < length:
        while len(table[i]) <=length:
            table[i].append("")

answer = ""
for c in range(length):
    for r in range(5):
        # if table[r][c]:
        answer += table[r][c]

print(answer)