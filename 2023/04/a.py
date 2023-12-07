import sys

def parse(s: str):
    return [int(x) for x in s.split(' ') if x.isdigit()]

ans = 0
for card in sys.stdin:
    card = card.strip()
    winning_numbers, owned_numbers = map(parse, card.split(':')[1].split('|'))

    shared_numbers = set(winning_numbers).intersection(owned_numbers)
    if len(shared_numbers):
        ans += 2 ** (len(shared_numbers) - 1)

print(ans)