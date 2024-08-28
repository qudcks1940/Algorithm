# 백준 1946 신입 사원 문제
import sys

input=sys.stdin.readline

T=int(input().strip())

for _ in range(T):
  N=int(input().strip())
  scores=[tuple(map(int,input().strip().split())) for _ in range(N)]
  scores.sort()

  count = 1
  min=scores[0][1]
  for i in range(1,N):
    if scores[i][1] < min:
      count+=1
      min=scores[i][1]
      
  print(count)
