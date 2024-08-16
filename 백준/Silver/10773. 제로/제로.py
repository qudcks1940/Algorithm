# 재현이가 잘못된 수를 부를때마다 0을 외쳐서,
# 재민이가 가장 최근에 쓴 수를 지우게 시킴.
# 모든 수를 받아 적은 후 그 수의 합

import sys

input = sys.stdin.readline

K = int(input().strip())

# numbers = [int(input().strip()) for _ in range(K)]

numbers=[]
for i in range(K):
  number = int(input().strip())
  if number==0:
    numbers.pop()
    continue
  numbers.append(number)
print(sum(numbers)) 
  