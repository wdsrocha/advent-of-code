import sys

def parse(s: str):
    return [int(x) for x in s.split(' ') if x.isdigit()]

ans = 0
cards = [card.strip() for card in sys.stdin]
buckets = [1]*len(cards)
for i, card in enumerate(cards):
    card = card.strip()
    winning_numbers, owned_numbers = map(parse, card.split(':')[1].split('|'))
    shared_numbers = set(winning_numbers).intersection(owned_numbers)

    print(f"Card {i + 1} has {len(shared_numbers)} shared numbers")

    n = min(len(cards), i + 1 + len(shared_numbers))
    for j in range(i + 1, n):
        print(f'Bucket {j + 1} gets +{buckets[i]}')
        buckets[j] += buckets[i]

print(sum(buckets))