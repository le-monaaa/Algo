# baekjoon 19532 수학은 비대면강의입니다 https://www.acmicpc.net/problem/19532
# a, b, c, d, e, f 가 주어질 때, 주어진 연립방정식을 만족하는 유일한 값 x,y 구하기

def simultaneous_equations(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                return x, y

a, b, c, d, e, f = map(int, input().split())

print(*(simultaneous_equations(a, b, c, d, e, f)))

