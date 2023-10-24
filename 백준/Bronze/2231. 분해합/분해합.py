N = int(input())
answer = 0

for num in range(1, N):
    if answer != 0:
        break
    if num + sum(list(map(int, list(str(num))))) == N:
        answer = num

print(answer)