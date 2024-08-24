# 백준 9252 LCS 2

import sys

input=sys.stdin.readline

s1=input().strip()
s2=input().strip()

str1=" "+s1
str2=" "+s2

table=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

# LCS 문자열을 저장할 리스트
lcs = [[""] * (len(s2) + 1) for _ in range(len(s1) + 1)]

# LCS 테이블 및 문자열 동시에 채우기
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if str1[i] == str2[j]:  # 문자가 일치하면
            table[i][j] = table[i - 1][j - 1] + 1
            lcs[i][j] = lcs[i - 1][j - 1] + str1[i]  # 대각선 방향에서 문자를 추가
        else:  # 문자가 일치하지 않으면
            if table[i - 1][j] >= table[i][j - 1]:
                table[i][j] = table[i - 1][j]
                lcs[i][j] = lcs[i - 1][j]  # 위쪽에서 가져온 값을 사용
            else:
                table[i][j] = table[i][j - 1]
                lcs[i][j] = lcs[i][j - 1]  # 왼쪽에서 가져온 값을 사용
# LCS 길이 출력
print(table[len(s1)][len(s2)])

# LCS 문자열 출력
print(lcs[len(s1)][len(s2)])