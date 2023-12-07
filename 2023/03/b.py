import sys

id = 0
cell_to_id = {}
numbers = {}
gears = []

for i, line in enumerate(sys.stdin):
    id += 1 # this will make some valid id non-sequential, but it does not matter
    for j, cell in enumerate(line):
        if cell.isdigit():
            cell_to_id[(i, j)] = id
            if not id in numbers:
                numbers[id] = int(cell)
            else:
                numbers[id] = numbers[id] * 10 + int(cell)
        else:
            id += 1
        
        if cell == '*':
            gears.append((i, j))

NORTH     = (-1, 0)
NORTHEAST = (-1, 1)
EAST      = ( 0, 1)
SOUTHEAST = ( 1, 1)
SOUTH     = ( 1, 0)
SOUTHWEST = ( 1,-1)
WEST      = ( 0,-1)
NORTHWEST = (-1,-1)

DIRECTIONS = [NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST]

ans = 0
for symbol in gears:
    part_number_ids = set()
    for direction in DIRECTIONS:
        adjacent_position = (symbol[0] + direction[0], symbol[1] + direction[1])
        if adjacent_position in cell_to_id:
            part_number_ids.add(cell_to_id[adjacent_position])
    
    if len(part_number_ids) == 2:
        first = numbers[part_number_ids.pop()]
        second = numbers[part_number_ids.pop()]
        ans += first * second 

print(ans)