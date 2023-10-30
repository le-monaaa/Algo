N = int(input())
count = 0
num = 666

while count != N:
    if "666" in str(num):
        if str(num).count("6") >= 3:
            count += 1
    num += 1

print(num-1)