import sys
from collections import deque
import heapq

input=sys.stdin.readline

N, M = map(int, input().strip().split())
# N x N 행렬 초기화 (모든 값은 0으로 설정)
matrix = [[0] * (N+1) for _ in range(N+1)]

# 사용자로부터 값을 입력받아 1행 1열부터 N행 M열까지 채우기
for i in range(1, N + 1):
    row_values = list(map(int, input().strip().split()))  # 문자열로 입력받음
    for j in range(1, N + 1):
        matrix[i][j] = int(row_values[j - 1])

S, X, Y = map(int,input().strip().split())

# N x N 크기의 graph 설정 (1부터 인덱싱)
graph = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

# 이동할 수 있는 4가지 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
          for k in range(4):
              ni, nj = i + dx[k], j + dy[k]
              if 1 <= ni <= N and 1 <= nj <= N:
                  graph[i][j].append((ni, nj))

def bfs():
  
  heap=[]
  for i in range(1, N+1):
      for j in range(1, N+1):
          if matrix[i][j]!=0:
              heapq.heappush(heap,(0,matrix[i][j],i,j))
  
  while heap:
    time, virus, x,y = heapq.heappop(heap)
    if time==S:
      break    
    # matrix 값이 0이라면 방문한 적이 없는거임.
    # 전염병이 아직 가지 않았다는 뜻 
    for i,j in graph[x][y]:
      if matrix[i][j]==0:
        matrix[i][j]=virus 
        heapq.heappush(heap,(time+1,virus,i,j))

bfs()
print(matrix[X][Y])