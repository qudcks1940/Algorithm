import sys

input = sys.stdin.readline

N, X = map(int, input().strip().split())

numbers = list(map(int,input().strip().split()))

# 파이썬에서 print는 출력하고 다음 줄로 가니까
# end를 잘 활용하자
for i in range(0,N):
  if(numbers[i] < X):
    print(numbers[i], end=" ")