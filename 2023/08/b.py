import sys
from math import lcm

instruction = sys.stdin.readline().strip("\n")
_ = sys.stdin.readline()  # empty line

machine = {}

sources = set()
destinations = set()

for line in sys.stdin:
    element, _, left_element, right_element = line.split(" ")
    left_element = left_element[1:4]
    right_element = right_element[:3]
    machine[element] = {"L": left_element, "R": right_element}

    if element.endswith("A"):
        sources.add(element)
    if element.endswith("Z"):
        destinations.add(element)


def run(source: str):
    head, node = 0, source

    memory = {}
    memory[f"{head}-{node}"] = 0

    reaches = []
    while True:
        key = f"{head}-{node}"
        # print(key)

        next_head = (head + 1) % len(instruction)
        next_node = machine[node][instruction[head]]
        next_key = f"{next_head}-{next_node}"

        if next_key in memory:
            return reaches

        memory[next_key] = memory[key] + 1

        if next_node.endswith("Z"):
            reaches.append(memory[next_key])

        node, head = next_node, next_head


values = []
for source in sources:
    value = run(source)
    values += value
    print(f"{source}: {value}")

print(lcm(*values))
