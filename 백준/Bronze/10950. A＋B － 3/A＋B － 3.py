import sys

input=sys.stdin.readline

n=int(input().strip())

for _ in range(n):
  nums=list(map(int,input().strip().split()))
  print(nums[0]+nums[1])