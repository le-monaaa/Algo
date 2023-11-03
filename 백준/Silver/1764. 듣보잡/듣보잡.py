# baekjoon 1764 https://www.acmicpc.net/problem/1764
# 듣도 보도 못한 사람의 명단 구하기

import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N: 듣도못한사람수 M: 보도못한사람수
didnt_hear = set()
didnt_see = set()

for n in range(N):
    didnt_hear.add(input().strip())

for m in range(M):
    didnt_see.add(input().strip())

ans = didnt_see&didnt_hear

ans = sorted(ans)
print(len(ans))
for person in ans:
    print(person)