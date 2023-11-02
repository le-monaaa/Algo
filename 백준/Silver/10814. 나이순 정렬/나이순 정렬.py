N = int(input())

members = []

for n in range(N):
    age, name = input().split()
    members.append([int(age), name])

members = sorted(members, key=lambda member: member[0])
for member in members:
    print(*member)