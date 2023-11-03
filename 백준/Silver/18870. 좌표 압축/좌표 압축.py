# 18870 좌표 압축 https://www.acmicpc.net/problem/18870
import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
sorted_nums = sorted(set(nums))

nums_dict = {sorted_nums[i]:i for i in range(len(sorted_nums))}
for i in range(N):
    print(nums_dict[nums[i]], end=" ")