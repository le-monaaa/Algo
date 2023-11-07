import sys
input = sys.stdin.readline

def sequence(selected):
    # 종료조건
    if len(selected) == M:
        print(*selected)
        return

    for n in range(1, N+1):
        if n not in selected:
            selected.append(n)
            sequence(selected)
            selected.pop()

N, M = map(int, input().split())

sequence([])