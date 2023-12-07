import sys
import re

def f(game, color):
    return max([int(x) for x in re.findall(f"(\d+) {color}", game)])

powers = []
for line in sys.stdin:
    red = f(line, 'red')
    green = f(line, 'green')
    blue = f(line, 'blue')
    powers.append(red * green * blue)


print(sum(powers))