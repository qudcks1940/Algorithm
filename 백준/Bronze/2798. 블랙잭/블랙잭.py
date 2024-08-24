import sys
import itertools

input = sys.stdin.readline

N, M = map(int,input().strip().split())

cards = list(map(int,input().strip().split()))

three_cards = itertools.combinations(cards, 3)

min_price = sys.maxsize
right_card = []
for card in three_cards:
    if sum(card) <= M:
        right_card.append(card)
        sub=M-sum(card)
        if sub < min_price:
            min_price = sub  
answer = M - min_price         
print(answer)
