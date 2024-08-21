# 백 준 2493번 탑 문제 스택 영역
# 문제풀이가 바로 떠오르지는 않지만,
# count로 어떻게 잘하면 될 것 같다.

import sys
from collections import deque

input=sys.stdin.readline

N=int(input().strip())

tops=list(map(int,input().strip().split()))

stack=[]
answers=[]

# 내가 신호를 쐈을때, 앞에 내 신호를 막는 타워들을 계속 스택에 쌓아서 유지함.
# 현재 탑보다 왼쪽에 있는데 현재 탑이 왼쪽의 타워보다 높으면
# 왼쪽의 타워는 스택에 있을 필요가 없음.

for i in range(N):
  current_height = tops[i]
# 스택이 비어있지 않고, 현재 탑이 스택의 마지막 탑보다 높은 경우
  while stack and stack[-1][1] < current_height:
      stack.pop()  # 스택에서 제거 (이 탑은 더 이상 신호를 수신할 수 없음)

  if stack:
      # 스택의 마지막 탑이 현재 탑의 신호를 수신할 수 있음
      answers.append(stack[-1][0] + 1)
  else:
      # 수신할 탑이 없을 경우
      answers.append(0)

    # 현재 탑을 스택에 추가 (인덱스는 0부터 시작하므로 i)
  stack.append((i, current_height))
while stack:
    stack.pop()
# 결과 출력
print(" ".join(map(str, answers)))



# 답은 나오지만 O(N^2)으로 시간초과
# answers=[]
# answer=0
# for i in range(N):
#   first_top=tops[-1]
#   for j in range(N-i-2,-1,-1):
#     if tops[j] > first_top:
#       answer=j+1
#       break
#   answers.append(answer)
#   answer=0  
#   tops.pop()

# print(' '.join(str(answers[i]) for i in answers))

