# baekjoon 10870 피보나치 수 https://www.acmicpc.net/problem/10870
# n번째 피보나치 수 재귀로 구하기

import sys
def fibonacci_numbers(n):
    # 종료조건
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

N = int(sys.stdin.readline())

ans = fibonacci_numbers(N)

print(ans)


