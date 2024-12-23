import sys

num1 = int(input())
num2 = input()

for i in range(int(len(num2))-1,-1,-1):
  print(num1*int(num2[i]))
print(num1*int(num2))

