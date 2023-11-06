import sys
input = sys.stdin.readline

while True:
    value = input().rstrip()
    ans = 0
    if value == ".":
        break
    stack = []
    for c in value:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
           if len(stack) < 1 or stack[-1] != "(":
               ans = 1
               break
           else:
               stack.pop()
        elif c == "]":
            if len(stack) < 1 or stack[-1] != "[":
                ans = 1
                break
            else:
                stack.pop()
    if ans == 0:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
    else:
        print("no")

