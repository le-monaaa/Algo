# baekjoon 18258 큐2 https://www.acmicpc.net/problem/18258
# queue 명령 처리

from sys import stdin
input = stdin.readline

N = int(input())
queue = [0] * (N+1)
front = 0
rear = 0
for n in range(N):
    command = input().rstrip()

    if command == "pop":
        # 큐에 정수가 없는 경우
        if front == rear:
            print("-1")
        else:
            print(queue[front])
            front += 1

    elif command == "size":
        print(rear-front)

    elif command == "empty":
        if front == rear:
            print("1")
        else:
            print("0")

    elif command == "front":
        if front == rear:
            print("-1")
        else:
            print(queue[front])

    elif command == "back":
        if front == rear:
            print("-1")
        else:
            print(queue[rear-1])

    else:
        a, b = command.split()
        queue[rear] = b
        rear += 1
