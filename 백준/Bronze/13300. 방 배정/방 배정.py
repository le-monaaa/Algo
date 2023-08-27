n, k = map(int, input().split()) # n: 학생 수 k: 최대 인원 수
grade = [[0] * 2 for _ in range(7)]

for i in range(n):
    s, g = map(int, input().split())
    # 학년 구분
    for b in range(7):
        if b == g:
            # 성별 구분
            if s == 0: # 여학생
                grade[g][0] += 1
            else:
                grade[g][1] += 1
# k로 나누기
room = 0
for i in range(7):
    for j in range(2):
        if grade[i][j] == 0:
            pass
        elif grade[i][j] <= k:
            room += 1
        else:
            room += grade[i][j]//k
            if grade[i][j]%k != 0:
                room += 1
print(room)