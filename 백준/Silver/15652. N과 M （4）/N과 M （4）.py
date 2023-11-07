# baekjoon 15652 N과 M(4) https://www.acmicpc.net/problem/15652
# 1부터 N까지 M개를 고른 수열. 중복 가능. 비내림차순.

import sys
input = sys.stdin.readline

def sequence(selected,start):
    if len(selected)== M:
        print(*selected)
        return

    for n in range(start, N+1):
        selected.append(n)
        sequence(selected, n)
        selected.pop()

N, M = map(int, input().split())

sequence([], 1)