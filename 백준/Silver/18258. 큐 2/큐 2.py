# 백 준 18258번 큐 2 문제 큐 영역
import sys
import queue
from collections import deque
input=sys.stdin.readline

N=int(input().strip())

myqueue = queue.Queue()

for i in range(N):
  command=input().strip().split()

  if command[0]=='push':
    myqueue.put(command[1])
  elif command[0]=='pop':
    if myqueue.qsize()==0:
      print(-1)
    else:
      print(myqueue.get())
  elif command[0]=='size':
    print(myqueue.qsize())
  elif command[0]=='empty':
    if not myqueue.empty():
      print(0)
    else:
      print(1)
  elif command[0]=='front':
    if myqueue.qsize()==0:
      print(-1)
    else:
      print(myqueue.queue[0])
  elif command[0]=='back':
    if myqueue.qsize()==0:
      print(-1)
    else:
      print(myqueue.queue[-1])