# baekjoon 27433 팩토리얼 https://www.acmicpc.net/problem/27433
# 팩토리얼 값 재귀로 구하기
import sys

def factorial_recursion(n):
    # 종료조건
    if n <= 1:
        return 1
    return n * factorial_recursion(n-1)

N = int(sys.stdin.readline())
ans = factorial_recursion(N)
print(ans)
