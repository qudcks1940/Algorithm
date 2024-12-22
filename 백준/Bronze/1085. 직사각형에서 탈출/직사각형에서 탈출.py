import sys


# map의 동작 원리에 대해 살펴보자.
# 한 줄에 여러 값 입력해서 리스트에 넣기
input = sys.stdin.readline
spot = list(map(int, input().split()))

r_distance = abs(spot[2]-spot[0])
l_distance = abs(spot[3]-spot[1])
x_distance = spot[0]
y_distance = spot[1]

distance = [x_distance, y_distance, r_distance, l_distance]

# 최소값 꺼내기 사용
min = sys.maxsize
for i in range(0,len(spot)):
  if(distance[i] < min):
    min = distance[i]
print(min)

