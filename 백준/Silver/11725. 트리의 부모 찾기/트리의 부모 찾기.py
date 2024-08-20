# 백 준 11725번 트리의 부모 찾기 문제

import sys

input=sys.stdin.readline

N=int(input().strip())

graph=[[] for _ in range(N+1)]
visited=[False] * (N+1)
parents=[0] * (N+1)

for _ in range(N-1):
  child1, child2 = map(int,input().strip().split())
  if graph[child1] == []:
    graph[child1] = [child2]
  else:
    graph[child1].append(child2)
  if graph[child2] == []:
    graph[child2] = [child1]
  else:
    graph[child2].append(child1)

def dfs_stack(graph, start, visited):
  stack=[start]
  root=1
  while stack:
    now=stack.pop()
    if not visited[now]:
      visited[now]=True
      for i in graph[now]:
        if not visited[i]:
          parents[i]=now
          stack.append(i)
dfs_stack(graph,1,visited)
for parent in parents[2:]:
  print(parent)