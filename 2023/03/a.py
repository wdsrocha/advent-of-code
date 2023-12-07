import sys

id = 0
cell_to_id = {}
numbers = {}
symbols = []

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
        
        if not cell.isdigit() and cell != '.' and cell != '\n':
            symbols.append((i, j))

NORTH     = (-1, 0)
NORTHEAST = (-1, 1)
EAST      = ( 0, 1)
SOUTHEAST = ( 1, 1)
SOUTH     = ( 1, 0)
SOUTHWEST = ( 1,-1)
WEST      = ( 0,-1)
NORTHWEST = (-1,-1)

DIRECTIONS = [NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST]

part_number_ids = set()
for symbol in symbols:
    for direction in DIRECTIONS:
        adjacent_position = (symbol[0] + direction[0], symbol[1] + direction[1])
        if adjacent_position in cell_to_id:
            part_number_ids.add(cell_to_id[adjacent_position])

ans = sum([numbers[id] for id in part_number_ids])
print(ans)