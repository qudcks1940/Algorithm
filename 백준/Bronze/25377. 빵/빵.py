import sys

input=sys.stdin.readline

N=int(input().strip())

min_time=[]
sum=0
for _ in range(N):
  A, B=map(int,input().strip().split())
  count=0

  
  if A <= B:
    min_time.append(B-A)
    sum+=B-A
  else:
    min_time.append(B-A)
    sum+=abs(B-A)
  for i in min_time:
    if i < 0:
      count+=1
if count==N:
  print(-1)
else:
  print(sum)
