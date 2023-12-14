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

lowest_location = -1
for i, seed in enumerate(seeds):
    print(f"Seed {i}: {seed}")
    for j, mapper in enumerate(mappers):
        print(f"\n{names[j]}")
        new_seed = seed
        for destination, source, range_length in mapper:
            print(f"{destination:02} {source:02} {range_length:02}")
            if source <= seed < source + range_length:
                new_seed = seed - source + destination
        print(f"Seed {seed} was mapped to {new_seed}")
        seed = new_seed

    if lowest_location == -1 or seed < lowest_location:
        lowest_location = seed

    print(f"Seed {i} location: {seed}\n")

print(lowest_location)
