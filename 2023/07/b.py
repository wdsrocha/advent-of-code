import sys
from collections import Counter
from enum import Enum


value = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
    "J": -1,  # :)
}


def trade_jokers(hand: str):
    counter = Counter(hand)
    if counter["J"] == 0:
        return hand
    if counter["J"] == 5:
        return "AAAAA"

    hand_without_jokers = "".join([card for card in hand if card != "J"])
    counter_without_jokers = Counter(hand_without_jokers)
    greatest_repetition = max(counter_without_jokers.values())

    highest_card = "J"
    for card in counter.keys():
        if counter[card] < greatest_repetition:
            continue

        if value[card] > value[highest_card]:
            highest_card = card

    new_hand = "".join([card if card != "J" else highest_card for card in hand])

    return new_hand


def g(hand: str) -> int:
    f = sorted(Counter(trade_jokers(hand)).values())
    if f == [5]:  # five of a kind
        return 6
    if f == [1, 4]:  # four of a kind
        return 5
    if f == [2, 3]:  # full house
        return 4
    if f == [1, 1, 3]:  # three of a kind
        return 3
    if f == [1, 2, 2]:  # two pairs
        return 2
    if f == [1, 1, 1, 2]:  # pair
        return 1
    return 0  # trash


game = []
for line in sys.stdin:
    hand, bid = line.split()
    # hand = trade_jokers(hand)
    bid = int(bid)
    game.append({"hand": hand, "bid": bid})


def compare_hands(a, b):
    a, b = a["hand"], b["hand"]
    if g(a) != g(b):
        return g(a) > g(b)

    for i, j in zip(a, b):
        if value[i] != value[j]:
            return value[i] > value[j]
    return True


def bubble_sort(arr, compare_func):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if compare_func(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(game, compare_hands)

ans = 0
for i, k in enumerate(game):
    if i and g(k["hand"]) > g(game[i - 1]["hand"]):
        print()
    print(k["hand"])
    ans += (i + 1) * k["bid"]

print(ans)
