import sys

input = sys.stdin.readline


heights = [int(input().strip()) for _ in range(9)]

two = sum(heights)-100

num1,num2 = 0,0

for i in range(len(heights)): 
    for j in range(len(heights)):
        if heights[i] + heights[j] == two:
          num1 = heights[i]
          num2 = heights[j]
          break
        
heights.remove(num1)
heights.remove(num2)


N = len(heights)

for j in range(N):
  k = N-j
  for i in range(1,k):
    if heights[i-1] >= heights[i]:
      temp = heights[i-1]
      heights[i-1] = heights[i]
      heights[i] = temp

# for height in heights:
#    print(height)
# print([i for i in range(len(heights))])
[print(i) for i in heights]
