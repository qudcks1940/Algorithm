import sys

input = sys.stdin.readline

# n = int(input())

numbers = [int(input()) for _ in range(9)]

count = 0
max = 0
for i in range(len(numbers)):
  if numbers[i] > max:
    max = numbers[i]
    count = i+1
print(max)
print(count)