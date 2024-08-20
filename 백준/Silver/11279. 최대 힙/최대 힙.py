# 백 준 11279번 최대 힙 문제
# Maxheap

# Minheap에 대해서도 알아보자

# import heapq, sys

# heap = []
# n = int(sys.stdin.readline())
# for i in range(n):
# 	num = int(sys.stdin.readline())
# 	if num == 0:
# 		if len(heap) == 0:
# 			print(0)
# 		else:
# 			print(heapq.heappop(heap))
# 	else:
# 		heapq.heappush(heap, num)


import heapq, sys

heap = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num == 0:
		if len(heap) == 0:
			print(0)
		else:
			print(-heapq.heappop(heap))
	else:
		heapq.heappush(heap, -num)