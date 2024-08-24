# 백준 9252 LCS 2

import sys

input=sys.stdin.readline

s1=input().strip()
s2=input().strip()

str1=" "+s1
str2=" "+s2

table=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

# LCS 테이블 및 문자열 동시에 채우기
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if str1[i] == str2[j]:  # 문자가 일치하면
            table[i][j] = table[i - 1][j - 1] + 1
        else:  # 문자가 일치하지 않으면
            if table[i - 1][j] >= table[i][j - 1]:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i][j - 1]
# LCS 길이 출력
print(table[-1][-1])




# dp=[[1] * (len(s1)+1) for _ in range(len(s2)+1)]

# a,b=0,0
# result=[]
# for i in range(1,len(s1)+1):
#   for j in range(1,len(s2)+1):
#     # dp[i][j] = dp[i][j] + 1
#     if j < b:
#       continue
#     if s1[i-1] == s2[j-1]:
#       dp[i][j] += dp[a][b]
#       result.append(s1[i-1])
#       a=i
#       b=j
#       # result.append()
#       break

# print(dp[a][b]-1)
# print(''.join(result))





