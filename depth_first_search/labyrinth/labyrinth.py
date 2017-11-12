from random import randint

SIZE = 20

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
        return ('column: ' + str(self.column) + ', row: ' + str(self.row) + ', visited: ' + str(self.visited) + '\n'+
        '↑'+str(self.top)+' →'+str(self.right)+' ↓'+str(self.bottom)+' ←'+str(self.left))

def index(column, row, size):
    if column < 0 or row < 0 or column > (size - 1) or row > (size - 1):
        return None
    return row + column * size

def nextNeighbour(columns, currentCell, size):
    column = currentCell.column
    row = currentCell.row

    neighbours = []

    topIndex = index(column-1, row, size)
    rightIndex = index(column, row+1, size)
    bottomIndex = index(column+1, row, size)
    leftIndex = index(column, row-1, size)

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
        if not cell.visited:
            return True
    return False


def generate(size=SIZE):
    grid = []
    for column in range(size):
        for row in range(size):
            grid.append(Cell(column, row))

    currentCell = grid[0]
    stack = []

    while hasUnvisited(grid):
        nextCell = nextNeighbour(grid, currentCell, size)
        if nextCell:
            stack.append(currentCell)
            removeWalls(currentCell, nextCell)
            nextCell.visited = True
            currentCell.visited = True
            currentCell = nextCell
        elif len(stack):
            currentCell = stack.pop()

    for cell in grid:
        cell.visited = False

    return grid