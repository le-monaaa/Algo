# beakjoon 행렬 덧셈
# N, M/ N lines M values

N, M = map(int, input().split())
list1 = []
list2 = []
for n in range(N):
    list1.append(list(map(int, input().split())))
for n in range(N):
    list2.append(list(map(int, input().split())))

for n in range(N):
    for m in range(M):
        list1[n][m] = list1[n][m] + list2[n][m]

for n in range(N):
    print(*list1[n])