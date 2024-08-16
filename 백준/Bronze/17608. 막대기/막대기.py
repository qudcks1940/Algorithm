# 백 준 17608번 막대기 문제 스택 영역
# 오른쪽에서 막대를 보았을때
# 몇 개가 보이는지 맞추기
# 뒤에 있는거 볼라면 길이가 무조건 길어야함.

import sys
from collections import deque
input=sys.stdin.readline


N=int(input().strip())

sticks = [int(input().strip()) for _ in range(N)]

first_stick = sticks[-1]
count=1
for i in range(len(sticks)-1,-1,-1):
  if sticks[i] > first_stick:
    first_stick = sticks[i]
    count+=1
print(count)