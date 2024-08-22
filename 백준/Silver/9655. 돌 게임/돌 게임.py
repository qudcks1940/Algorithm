# 백준 9655 돌 게임
n = int(input())

dp = [-1]*10001

dp[1] = 1 #SK
dp[2] = 0 #CY
dp[3] = 1 #SK

for i in range(4,n+1):
    if dp[i-1] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n]==1:
    print('SK')
else:
    print('CY')