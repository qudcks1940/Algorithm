# 2169 로봇 조종하기
# Tabulation 방식 중에
# gridTraveler, canSum, howSum, bestSum, 
# canconstruct, countconstruct 방식 중에
# gridTraveler 채택
# 문제 특성상 여러 방향에서 온 값을 고려해서 최대값을 계산해야하므로
# 테이블을 사용해 모든 하위 문제를 해결해가는 tabulation이 적합
# 3차원...?

import sys

input=sys.stdin.readline

N,M=map(int,input().strip().split())

# 원래 주어진 이차원 행렬 값
matrix=[list(map(int,input().strip().split())) for _ in range(N)]

# 첫째 줄 우측으로 쭉 다 더한 값을 맨 첫 줄에 나열
dp=[[0]*(M) for _ in range(N)]

dp[0][0]=matrix[0][0]

for j in range(1,len(matrix[0])):
  dp[0][j] = dp[0][j-1] + matrix[0][j]

for i in range(1,N):
  # Ldp의 첫 값과 Rdp의 첫 값은 그냥 대입 왜냐하면
  # 맨 왼쪽의 첫 번째 값과 맨 오른쪽의 첫 번째 값은 
  # 전에서 넘어올 값이 없기 때문이다.
  Ldp, Rdp = [0]*M,[0]*M
  Ldp[0] = dp[i-1][0] + matrix[i][0]
  Rdp[-1] = dp[i-1][-1] + matrix[i][-1]
  for j in range(1,M):
    # 만약에 맨 첫 줄에서도 우측으로 가다가 아랫쪽이 더 값이 높다면
    # 아래 쪽을 선택할 수도 있음.
    # Ldp는 윗줄 맨왼쪽에서 넘어온 값부터 우측으로 쭉 가는 리스트
    # Rdp는 윗줄 맨오른쪽에서 넘어온 값부터 좌측으로 쭉 가는 리스트
    # 그러니까 Ldp는 맨 첫 번째 값에서 바로 아래로 내려오니까
    # 첫 번째 줄은 무조건 오른쪽으로 간다는 말은 틀림.
    # 어쨌든 비교를 한다는 말.
    Ldp[j] = max(Ldp[j-1], dp[i-1][j]) + matrix[i][j]
    Rdp[-1-j] = max(Rdp[-j], dp[i-1][-1-j]) + matrix[i][-1-j]
  for j in range(M):
    dp[i][j] = max(Ldp[j],Rdp[j])
print(dp[-1][-1])