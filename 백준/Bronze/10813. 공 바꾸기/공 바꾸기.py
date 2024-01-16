n, m = map(int, input().split())
alist = [i for i in range(1, n+1)]

for i in range(0, m):
    a, b = map(int, input().split())
    alist[a-1], alist[b-1] = alist[b-1], alist[a-1]

for a in range(0, n):
    print(alist[a], end = " ")