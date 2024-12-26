import sys

input = sys.stdin.readline

A, B, C = map(int,[input().strip() for _ in range(3)])

number = [int(digit) for digit in str(A*B*C)]

frequent=0
for i in range(0,10):
  print(number.count(i))
