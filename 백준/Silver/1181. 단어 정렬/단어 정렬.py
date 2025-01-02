import sys

input=sys.stdin.readline

N=int(input().strip())

words=[input().strip() for i in range(N)]


min=sys.maxsize
leng=[]
stack=[]
for i in words:
  stack.append((len(i),i))

answer=[]
for j in sorted(set(stack)):
  print(j[1])