import sys

input=sys.stdin.readline

T=int(input().strip())

for _ in range(T):
  numbers=tuple(map(int,input().strip().split()))

  count=0
  for i in range(1, numbers[0]+1):
    for j in range(1, numbers[1]+1):
      for k in range(1, numbers[2]+1):
        if i % j == j % k and j % k == k % i:
          count+=1

  print(count)
