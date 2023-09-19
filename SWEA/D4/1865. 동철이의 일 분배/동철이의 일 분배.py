def backTracking(row, col, now_percentage, a):
    global max_percentage
    # 종료
    if row == N:
        if max_percentage < now_percentage:
            max_percentage = now_percentage

        return

    # 반복
    for i in range(N):
        if i not in col:
            temp = now_percentage
            now_percentage *= task[row][i]
            if now_percentage > max_percentage:
                col.append(i)
                a.append(task[row][i])
                backTracking(row + 1, col, now_percentage, a)
                col.remove(i)
                a.remove(task[row][i])
            now_percentage = temp


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 직원수/업무의수
    task = []
    for n in range(N):
        task.append(list(map(int, input().split())))

    max_percentage = 0

    for i in range(N):
        for j in range(N):
            task[i][j] *= 0.01


    backTracking(0, [], 1, [])
    
    print(f"#{tc}", "{:.6f}".format(round(max_percentage * 100, 6)))