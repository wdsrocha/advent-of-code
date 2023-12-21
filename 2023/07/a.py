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
}


def g(hand: str) -> int:
    f = sorted(Counter(hand).values())
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
    print(k["hand"])
    ans += (i + 1) * k["bid"]

print(ans)
