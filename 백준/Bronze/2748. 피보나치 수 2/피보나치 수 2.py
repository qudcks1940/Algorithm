# 백준 2748 피보나치 수 2

import sys

input=sys.stdin.readline

dp=[0]*91

N=int(input().strip())
dp[0]=0
dp[1]=1

for i in range(2,N+1):
  dp[i]=dp[i-1]+dp[i-2]

print(dp[N])