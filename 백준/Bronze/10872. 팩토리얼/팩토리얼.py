import sys

input = sys.stdin.readline

def fact(n:int) -> int:
  if n > 0:
    return n*fact(n-1)
  elif n == 0:
    return 1
  else:
    return 0

N = int(input().strip())

print(fact(N))
