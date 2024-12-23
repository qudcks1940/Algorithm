# 백 준 2739번 
# 구구단 
# 브론즈 5

#2024-12-23 풀이
import sys

input=sys.stdin.readline

number=int(input().strip())

for i in range(1,10):
  print(str(number)+" * "+str(i)+" = "+str(number*i))