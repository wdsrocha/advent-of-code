import sys

instruction = sys.stdin.readline().strip("\n")
_ = sys.stdin.readline()  # empty line

machine = {}

for line in sys.stdin:
    element, _, left_element, right_element = line.split(" ")
    left_element = left_element[1:4]
    right_element = right_element[:3]
    machine[element] = {"L": left_element, "R": right_element}

node = "AAA"
head = 0
steps = 0
while node != "ZZZ":
    steps += 1
    node = machine[node][instruction[head]]
    head = (head + 1) % len(instruction)

print(steps)
