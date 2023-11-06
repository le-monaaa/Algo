import sys
input = sys.stdin.readline

N = int(input())
stack = [0] * N
index = 0

for n in range(N):
    value = input().strip()

    if value == "2":
        # 스택에 정수가 없으면 index = 0
        if index == 0:
            print(-1)
        else:
            index -= 1
            print(stack[index])

    elif value == "3":
        print(index)
    elif value == "4":
        if index == 0:
            print(1)
        else:
            print(0)
    elif value == "5":
        if index == 0:
            print(-1)
        else:
            print(stack[index-1])
    else:
        a, b = value.split()
        stack[index] = int(b)
        index += 1