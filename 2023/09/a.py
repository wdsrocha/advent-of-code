import sys


def extrapolate(a: list):
    if len(a) == 1:
        return a[-1]
    b = [a[i] - a[i - 1] for i in range(1, len(a))]
    return a[-1] + extrapolate(b)


total = 0
for line in sys.stdin:
    total += extrapolate([int(x) for x in line.split()])

print(total)
