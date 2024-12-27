import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))

count = 0
for i in numbers:
    if i <= 1:
        continue
    elif i == 2:
        count += 1
    elif i % 2 == 0:
        continue
    else:
        is_prime = True
        for j in range(2, i):  # 2부터 i-1까지 검사
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print(count)