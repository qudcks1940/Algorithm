# 백 준 2798
# 블랙잭

import sys
import itertools

N, M=list(map(int,input().strip().split()))

numbers=list(map(int,input().strip().split()))

three=itertools.combinations(numbers,3)

isCheck=False
max=0

for i in three:
  sum=0
  for j in i:
    sum+=j
  if sum==M:
    isCheck=True
    print(M)
    break
  elif max<M and sum>max and sum<M:
    max=sum

if isCheck==False:
  print(max)
  
