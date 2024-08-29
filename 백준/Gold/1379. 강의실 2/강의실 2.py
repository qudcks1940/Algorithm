# 틀렸습니다,,

import sys
import heapq

input=sys.stdin.readline

K = int(input())

lectures = [list(map(int, input().split())) for _ in range(K)]
lectures.sort(key = lambda x: x[1])

heap = []
heapq.heappush(heap, (lectures[0][2],1))

answer= 1
room = 1
result = [0]*(K+1)

# 처음 강의는 1번 강의실에 배정
result[lectures[0][0]] = 1

for num, start, end in lectures[1:]:
    if heap[0][0] > start:
        heapq.heappush(heap, (end, room+1))
        room += 1
        result[num] = room
        answer += 1
    else:
        while heap[0][0] > start:
            heapq.heappop(heap)
        end_time, room_num = heapq.heappop(heap)
        result[num] = room_num
        heapq.heappush(heap, (end, room_num))
print(answer)
for i in range(1, K+1):
    print(result[i])