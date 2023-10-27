
color_case = ["WBWBWBWB", "BWBWBWBW"]
N, M = map(int, input().split()) # N * M 배열
table = [input() for _ in range(N)]
min_count = 64
i, j = 0, 0
num = 0

for r in range(N-7):
    for c in range(M-7):
        count_a, count_b = 0, 0
        for i in range(8):
            for j in range(8):
                if (i+1)%2 == 0:
                    if table[r + i][c + j] != color_case[0][j]:
                        count_a += 1
                    if table[r + i][c + j] != color_case[1][j]:
                        count_b += 1
                else:
                    if table[r + i][c + j] != color_case[0][j]:
                        count_b += 1
                    if table[r + i][c + j] != color_case[1][j]:
                        count_a += 1
        min_c = count_a if count_a<=count_b else count_b

        if min_c < min_count:
            min_count = min_c

print(min_count)

# 오타주의하기