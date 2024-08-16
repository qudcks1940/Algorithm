import sys

input = sys.stdin.readline

# 입력 받을 숫자의 개수
K = int(input().strip())

stack = []

for _ in range(K):
    num = int(input().strip())
    if num == 0:
        stack.pop()  # 최근 입력된 숫자를 제거
    else:
        stack.append(num)  # 숫자를 스택에 추가

# 스택에 남아 있는 모든 수의 합 계산
print(sum(stack))
