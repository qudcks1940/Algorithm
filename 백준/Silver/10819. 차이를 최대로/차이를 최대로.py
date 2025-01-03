import sys
import itertools

N=int(input().strip())

numbers=list(map(int,input().strip().split()))

all=itertools.permutations(numbers,N)

max=0
for i in all:
  sum=0
  for j in range(len(i)-1):
    sum+=abs(i[j]-i[j+1])
  if sum>max:
    max=sum
print(max)
