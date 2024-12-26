import sys

input=sys.stdin.readline

numbers=input().strip().split()

n1=[]
for i in numbers[0]:
  n1.append(i)

n2=[]
for j in numbers[1]:
  n2.append(j)

r1=reversed(n1)
r2=reversed(n2)

r1_join=''.join(r1)
r2_join=''.join(r2)

if int(r1_join)>int(r2_join):
  print(r1_join)
else:
  print(r2_join)