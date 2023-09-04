n, m = map(int, input().split())
alist = [i for i in range(1, n+1)]
for i in range(0, m):
    f, t = map(int, input().split())
    temp = alist[f-1: t ]
    temp.reverse()
    alist[f-1: t] =temp

for i in range(0, n):
    print(alist[i], end = " ")
