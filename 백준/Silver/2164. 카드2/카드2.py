import sys
import queue
from collections import deque
input=sys.stdin.readline

N=int(input().strip())

myqueue = queue.Queue()

for i in range(1,N+1):
  myqueue.put(i)

while myqueue.qsize() >1:
  myqueue.get()
  myqueue.put(myqueue.get())

print(myqueue.get())

