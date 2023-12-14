import sys

seeds = []
mappers = []
current_mapper = -1
for line in sys.stdin:
    if line.startswith("seeds"):
        seeds = [int(x) for x in line[7:].split(" ")]
    elif "map" in line:
        current_mapper += 1
        mappers.append([])
    elif line != "\n":
        destination, source, range_length = [int(x) for x in line.split(" ")]
        mappers[current_mapper].append((destination, source, range_length))

names = [
    "seed to soil",
    "soil to fertilizer",
    "fertilizer to water",
    "water to light",
    "light to tempreature",
    "temperature to humidity",
    "humidity to location",
]

print(f"Seeds: {seeds}")

found = False
answer = 0

# https://www.youtube.com/watch?v=FgXYzF5-Yiw
while not found:
    location = answer
    for mapper in reversed(mappers):
        new_location = location
        for source, destination, range_length in mapper:
            if source <= location < source + range_length:
                new_location = location - source + destination
        location = new_location

    for i in range(0, len(seeds), 2):
        if seeds[i] <= location < seeds[i] + seeds[i + 1]:
            print(answer)
            found = True

    answer += 1
