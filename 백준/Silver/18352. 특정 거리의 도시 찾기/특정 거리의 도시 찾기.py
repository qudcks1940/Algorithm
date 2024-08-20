# 백 준 18352번 특정 거리의 도시 찾기 문제
from collections import deque
import sys

input=sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
# for i in range(len(graph)):
#   graph[i].sort()

from collections import deque

cost=[-1]*(n+1)
cost[x]=0
def bfs(graph, i, visited):
  queue= deque([i])
  visited[i]=True
  while queue:
    value = queue.popleft()
    for j in graph[value]:
      if not visited[j]:
        visited[j] = True
        cost[j] = cost[value]+1
        queue.append(j)
bfs(graph, x, visited)
found=False
for i in range(1,n+1):
  if cost[i]==k:
    print(i)
    found=True

if not found:
  print(-1)