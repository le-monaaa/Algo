# baekjoon 10773 제로 https://www.acmicpc.net/problem/10773
# 잘못된 수 입력시 0 입력, 가장 마지막 수 지움

import sys
input=sys.stdin.readline

K = int(input())
stack = [0] * K
index = 0
for k in range(K):
    value = input().strip()
    if value == "0":
        index -= 1

    else:
        stack[index] = int(value)
        index += 1

print(sum(stack[:index]))