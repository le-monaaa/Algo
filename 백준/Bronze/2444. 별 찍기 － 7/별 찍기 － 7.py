n = int(input())

space = n-1
star = 1
for i in range(1, n+1):
    print(" "*space, end= "")
    print("*"*( i * 2 -1))
    space -= 1
space = 1
for i in range(n-1, 0, -1):
    print(" "*space, end = "")
    print("*"*(i * 2 - 1))
    space += 1
