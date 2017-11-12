from PIL import Image, ImageDraw

WIDTH = 600
HEIGHT = 600

def drawCell(cellHeight, cellWidth, cell, draw, color=(128, 128, 128)):
    column = cell.column
    row = cell.row

    top =    ((cellWidth * column,       cellHeight * row),
              (cellWidth * (column + 1), cellHeight * row))
    right =  ((cellWidth * (column + 1), cellHeight * row),
              (cellWidth * (column + 1), cellHeight * (row + 1)))
    bottom = ((cellWidth * column,       cellHeight * (row+1)),
              (cellWidth * (column + 1), cellHeight * (row+1)))
    left =   ((cellWidth * column,       cellHeight * row),
              (cellWidth * column,       cellHeight * (row + 1)))
    if cell.top:
        draw.line(top, fill=color)
    if cell.bottom:
        draw.line(bottom, fill=color)
    if cell.right:
        draw.line(right, fill=color)
    if cell.left:
        draw.line(left, fill=color)

def draw(labyrinth, columns, rows):
    image = Image.new("RGBA", (WIDTH+1, HEIGHT+1), (51, 51, 51, 0))
    draw = ImageDraw.Draw(image)

    cellWidth = WIDTH // columns
    cellHeight = HEIGHT // rows

    for cell in labyrinth:
        drawCell(cellHeight, cellWidth, cell, draw)
    image.show()


if __name__ == '__main__':
    pass