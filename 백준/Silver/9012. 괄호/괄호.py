# 백 준 9012번 괄호문제 스택 영역
# 괄호 문자열(Parenthesis String, PS)은 '('와')'로만 구성된 문자열
# 괄호의 모양이 바르게 구성된 문자열 : 올바른 괄호 문자열 (Valid PS, VPS)
# 한 쌍의 "()"문자열은 기본 VPS라 한다.
# 만약 x가 VPS라면 (x)도 VPS가 됨.
# 두 VPS x와 y를 접합시킨 새로운 문자열 xy도 VPS가 됨.
# "(())()"와 "((()))"는 VPS,
# “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열
# 입력에 따라 VPS이면 YES
# 아니라면 NO
# 바로 든 생각은 입력된 문자열길이가 홀수면 무조건 VPS가 아니니까
# 홀수 짝수 나눠서 짝수 개수인 경우만 따져주는 것도 괜찮을 듯
import sys
from collections import deque
input = sys.stdin.readline

T=int(input().strip())

PS = [input().strip() for _ in range(T)]

for ps in PS:
  stack = deque()
  is_valid=True
  for char in ps:
    if char=='(':
      stack.append(char)
    elif char ==')':
      if stack:
        stack.pop()
      else:
        is_valid=False
        break
  
  if is_valid and not stack:
    print("YES")
  else:
    print("NO")