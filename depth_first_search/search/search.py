from labyrinth.labyrinth import hasUnvisited, index

def nextNeighbour(columns, currentCell, size):
    column = currentCell.column
    row = currentCell.row

    neighbours = []

    topIndex = index(column , row - 1, size)
    rightIndex = index(column + 1, row, size)
    bottomIndex = index(column, row + 1, size)
    leftIndex = index(column - 1, row, size)

    top = columns[topIndex] if topIndex else None
    right = columns[rightIndex] if rightIndex else None
    bottom = columns[bottomIndex] if bottomIndex else None
    left = columns[leftIndex] if leftIndex else None

    if (not currentCell.top) and top and (not top.visited):
        neighbours.append(top)

    if (not currentCell.right) and right and (not right.visited):
        neighbours.append(right)

    if (not currentCell.bottom) and bottom and (not bottom.visited):
        neighbours.append(bottom)

    if (not currentCell.left) and left and (not left.visited):
        neighbours.append(left)

    if len(neighbours):
        return neighbours[0]
    else:
        return None

def search(labyrinth, size):
    currentCell = labyrinth[0]
    stack = []

    while hasUnvisited(labyrinth):
        if currentCell.column == size - 1 and currentCell.row == size - 1:
            stack.append(currentCell)
            break
        nextCell = nextNeighbour(labyrinth, currentCell, size)
        if nextCell:
            stack.append(currentCell)
            nextCell.visited = True
            currentCell.visited = True
            currentCell = nextCell
        elif len(stack):
            currentCell = stack.pop()

    return stack

