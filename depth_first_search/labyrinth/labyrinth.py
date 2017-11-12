from random import randint

SIZE = 10

class Cell:
    def __init__(self, column, row):

        self.column = column
        self.row = row

        self.top = True
        self.left = True
        self.bottom = True
        self.right = True

        self.visited = False

    def __str__(self):
        return 'column: ' + str(self.column) + ', row: ' + str(self.row) + ', visited: ' + str(self.visited)

def index(column, row):
    if column < 0 or row < 0 or column > (SIZE - 1) or row > (SIZE - 1):
        return None
    return row + column * SIZE

def nextNeighbour(columns, currentCell):
    column = currentCell.column
    row = currentCell.row

    neighbours = []

    topIndex = index(column-1, row)
    rightIndex = index(column, row+1)
    bottomIndex = index(column+1, row)
    leftIndex = index(column, row-1)

    top = columns[topIndex] if topIndex else None
    right = columns[rightIndex] if rightIndex else None
    bottom = columns[bottomIndex] if bottomIndex else None
    left = columns[leftIndex] if leftIndex else None

    if top and not top.visited:
        neighbours.append(top)
    if right and not right.visited:
        neighbours.append(right)
    if bottom and not bottom.visited:
        neighbours.append(bottom)
    if left and not left.visited:
        neighbours.append(left)
    if len(neighbours):
        return neighbours[randint(0, len(neighbours)-1)]
    else:
        return None



def removeWalls(currentCell, nextCell):
    x = currentCell.column - nextCell.column
    y = currentCell.row - nextCell.row

    if x == 1:
        currentCell.left = False
        nextCell.right = False
    elif x == -1:
        nextCell.left = False
        currentCell.right = False
    if y == 1:
        currentCell.top = False
        nextCell.bottom = False
    elif y == -1:
        nextCell.top = False
        currentCell.bottom = False

def hasUnvisited(grid):
    for cell in grid:
        print(cell)
        if not cell.visited:
            return True
    return False


def generate():
    grid = []
    for i in range(SIZE):
        for j in range(SIZE):
            grid.append(Cell(i, j))

    currentCell = grid[0]
    stack = []

    while hasUnvisited(grid):
        nextCell = nextNeighbour(grid, currentCell)
        if nextCell:
            stack.append(currentCell)
            removeWalls(currentCell, nextCell)
            nextCell.visited = True
            currentCell.visited = True
            currentCell = nextCell
        elif len(stack):
            currentCell = stack.pop()

    return grid