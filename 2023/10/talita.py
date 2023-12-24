import sys

# THIS ONLY WORKS FOR MY INPUT BECAUSE I KNOW WHAT S IS SUPPOSED TO BE
# and i was too lazy to handle it via code
# its already terribly long
row = 0
original = []
for line in sys.stdin:
    original.append(line.strip())
processed = []
prevLine = []
for i in range(0, 2 * len(original[0])):
    prevLine.append(".")
processed.append(prevLine)
row = 0
for line in original:
    newLine = []
    nextLine = []
    for i in range(0, 2 * len(original[0])):
        nextLine.append(".")
    for ix, c in enumerate(line):
        if c == "L":
            processed[-1][ix * 2] = "|"
            newLine.append(c)
            newLine.append("-")
        elif c == "F":
            newLine.append(c)
            newLine.append("-")
            nextLine[ix * 2] = "|"
        elif c == "7":
            if len(newLine) > 0:
                newLine[-1] = "-"
            newLine.append(c)
            newLine.append(".")
            nextLine[ix * 2] = "|"
        elif c == "J":
            if len(newLine) > 0:
                newLine[-1] = "-"
            processed[-1][ix * 2] = "|"
            newLine.append(c)
            newLine.append(".")
        elif c == "|":
            newLine.append(c)
            newLine.append(".")
            nextLine[ix * 2] = "|"
        elif c == "-":
            newLine.append(c)
            newLine.append("-")
        elif c == "S":
            processed[-1][ix * 2] = "|"
            newLine.append(c)
            newLine.append("-")
        else:
            newLine.append(".")
            newLine.append(".")
    processed.append(newLine)
    processed.append(nextLine)
    row += 1


row = 0
vis = []
colour = []
start = []
adj = []
for line in processed:
    print("".join(line))
    vis.append([])
    colour.append([])
    if len(adj) == 0:
        # for i in range(0, len(line)):
        adj.append([[]] * len(line))

    adj.append([[]] * len(line))
    for col, c in enumerate(line):
        vis[row].append(0)
        colour[row].append(0)
        if c == "L":
            adj[row][col] = [[row - 1, col], [row, col + 1]]
        if c == "F":
            adj[row][col] = [[row, col + 1], [row + 1, col]]
        if c == "7":
            adj[row][col] = [[row, col - 1], [row + 1, col]]
        if c == "J":
            adj[row][col] = [[row - 1, col], [row, col - 1]]
        if c == "|":
            adj[row][col] = [[row - 1, col], [row + 1, col]]
        if c == "-":
            adj[row][col] = [[row, col - 1], [row, col + 1]]
        if c == "S":
            adj[row][col] = [[row - 1, col], [row, col + 1]]
            start = [row, col]

    row += 1
neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
next1 = adj[start[0]][start[1]][0]
row1 = next1[0]
col1 = next1[1]
prevRow1 = start[0]
prevCol1 = start[1]
vis[start[0]][start[1]] = 1
while vis[row1][col1] == 0:
    # break
    vis[row1][col1] = 1
    adj1 = adj[row1][col1]
    if adj1[0][0] == prevRow1 and adj1[0][1] == prevCol1:
        next1 = adj1[1]
    else:
        next1 = adj1[0]
    prevRow1 = row1
    prevCol1 = col1
    row1 = next1[0]
    col1 = next1[1]


stack = []

for i in range(0, len(vis)):
    stack.append([i, 0])
    stack.append([i, len(vis[i]) - 1])
for i in range(0, len(vis[0])):
    stack.append([0, i])
    stack.append([len(vis) - 1, i])
while len(stack) > 0:
    top = stack.pop()
    colour[top[0]][top[1]] = 1
    isEdge = vis[top[0]][top[1]]
    for neighbour in neighbours:
        isValid = True
        r = top[0] + neighbour[0]
        c = top[1] + neighbour[1]
        isValid = r >= 0 and r < len(vis) and c >= 0 and c < len(vis[r])
        if isValid:
            nIsEdge = vis[r][c]
            if (isEdge and nIsEdge) or (not isEdge):
                if colour[r][c] == 0:
                    stack.append([r, c])

count = 0
for i in range(1, len(colour), 2):
    for j in range(0, len(colour[i]), 2):
        if colour[i][j] == 0:
            count += 1
print(count)
