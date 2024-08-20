# 백 준 1707번 이분 그래프 문제
from collections import deque
import sys

input=sys.stdin.readline

K = int(input().strip())

group_seperate=[-1,1]
def dfs_stack(graph, i, group):
  stack=[i]
  group[i] = group_seperate[0]
  while stack:
    value=stack.pop()
    # 팝한 애들의 인접 노드들이 j에 담김.  
    for j in graph[value]:
      # group[j]에 값이 있는지 없는지 확인
      # group[j]에 값이 있는지 없는지 체크하는 이유 : none인 경우엔 비교 불가
      if group[j] == None:
        group[j] = -group[value]
        stack.append(j)
      elif group[j] == group[value]:
          return False
  return True

for _ in range(K):
    # 각 테스트 케이스의 정점 수 V와 간선 수 E 입력
    V, E = map(int, input().strip().split())
    
    # 그래프를 인접 리스트로 표현하기 위해 빈 리스트 생성
    graph = [[] for _ in range(V + 1)]
    group = [None for _ in range(V + 1)]
    
    for _ in range(E):
        # 각 간선 정보를 입력 받아 그래프에 추가
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    is_bipartite = True  # 이분 그래프 여부를 확인하는 플래그
    
    for node in range(1, V + 1):
        if group[node] is None:  # 방문하지 않은 모든 노드에 대해 DFS 시도
            if not dfs_stack(graph, node, group):
                is_bipartite = False
                break
    
    print("YES" if is_bipartite else "NO")




