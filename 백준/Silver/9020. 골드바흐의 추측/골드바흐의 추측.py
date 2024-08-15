import sys

# 2를 제외한 모든 짝수는 소수가 아님.
def sieve_of_eratosthenes(end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(end**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

input = sys.stdin.readline

N = int(input().strip())

numbers = [int(input().strip()) for _ in range(N)]
# numbers = list(map(int,input().strip().split()))

for number in numbers:
  # number보다 작은 수들 중 소수들을 찾아서 list화
  list_sieve = sieve_of_eratosthenes(number)

  # list_sieve에 number-1 까지의 소수들이 담겨 있으니까
  # 내부 소수들로 number를 만드는 for문을 짜야함.
  left, right = 0, len(list_sieve) - 1
  best_pair = (None, None)
  min_diff = float('inf')

  while left <= right:
      prime_sum = list_sieve[left] + list_sieve[right]

      if prime_sum == number:
          diff = list_sieve[right] - list_sieve[left]
          if diff < min_diff:
              min_diff = diff
              best_pair = (list_sieve[left], list_sieve[right])
          left += 1
          right -= 1
      elif prime_sum < number:
          left += 1
      else:
          right -= 1
  print(f'{best_pair[0]} {best_pair[1]}')
