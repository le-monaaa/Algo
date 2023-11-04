# baekjoon 7785 회사에 있는 사람 https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

N = int(input())
status = {}
for n in range(N):
    name, stat = input().split()
    status[name] = stat

sorted_status = dict(sorted(status.items(), reverse=True))
for key, value in sorted_status.items():
    if value == "enter":
        print(key)