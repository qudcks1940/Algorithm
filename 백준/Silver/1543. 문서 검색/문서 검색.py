import sys

input=sys.stdin.readline

text=input().strip()

target=input().strip()


count=0
target_len=len(target)

i=0
while i<len(text):
  if text[i:i+target_len]==target:
    i+=target_len
    count+=1
  else:
    i+=1

print(count)
