import sys

input=sys.stdin.readline

N=int(input().strip())

min_B=sys.maxsize
isKOI=False
for _ in range(N):
    A, B=map(int,input().strip().split())
    if A <= B:
        isKOI=True
        if B < min_B:
            min_B=B
     
if isKOI==False:
    print(-1)
else:
    print(min_B)
