# baekjoon 15651 N과 M(3) https://www.acmicpc.net/problem/15651
# 1부터 M까지 자연수 중에서 M개를 고른 수열. 중복도 가능. 사전 순으로 증가하는 순서로 출력

import sys
input = sys.stdin.readline

def sequence(selected):
    # 종료 조건
    if len(selected) == M:
        print(*selected)
        return

    for n in range(1, N+1):
        selected.append(n)
        sequence(selected)
        selected.pop()

N, M = map(int, input().split())

sequence([])