import sys

input=sys.stdin.readline

input = sys.stdin.readline

C = int(input().strip())

for _ in range(C):
  rows = list(map(int,input().strip().split()))
  N=rows[0]
  scores=rows[1:N+1]
  avg=sum(scores)/N
  count=0
  for score in scores:
    if score>avg:
      count+=1
  result=(count/N)*100
  print(f"{result:.3f}%")