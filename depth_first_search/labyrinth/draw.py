from PIL import Image, ImageDraw, ImageFont

WIDTH = 600
HEIGHT = 600

def drawCell(cellHeight, cellWidth, cell, draw, solution = [], color=(255, 128, 128)):
    column = cell.column
    row = cell.row

    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 15)

    if cell.top:
        top = ((cellWidth * column,       cellHeight * row),
              (cellWidth * (column + 1), cellHeight * row))
        draw.line(top, fill=color)
    if cell.bottom:
        bottom = ((cellWidth * column, cellHeight * (row + 1)),
                  (cellWidth * (column + 1), cellHeight * (row + 1)))
        draw.line(bottom, fill=color)
    if cell.right:
        right = ((cellWidth * (column + 1), cellHeight * row),
                 (cellWidth * (column + 1), cellHeight * (row + 1)))
        draw.line(right, fill=color)
    if cell.left:
        left = ((cellWidth * column, cellHeight * row),
                (cellWidth * column, cellHeight * (row + 1)))
        draw.line(left, fill=color)

    if cell in solution:
        draw.arc(
            [(cellWidth * column + cellWidth // 3, cellHeight * row + cellHeight // 3),
            (cellWidth * (column + 1) - cellWidth // 3, cellHeight * (row + 1) - cellHeight // 3)],
            start=0,
            end=360,
            fill=(255, 255, 255, 255))

def draw(labyrinth, size):
    image = Image.new("RGBA", (WIDTH+1, HEIGHT+1), (51, 51, 51, 0))
    draw = ImageDraw.Draw(image)

    cellWidth = WIDTH // size
    cellHeight = HEIGHT // size

    for pos in range(len(labyrinth)):
        drawCell(cellHeight, cellWidth, labyrinth[pos], draw)
    image.show()


def drawSolution(labyrinth, solution, graphSize, imageSize=WIDTH):
    image = Image.new("RGBA", (imageSize + 1, imageSize + 1), (51, 51, 51, 0))
    draw = ImageDraw.Draw(image)

    cellWidth = imageSize // graphSize
    cellHeight = imageSize // graphSize

    for cell in labyrinth:
        drawCell(cellHeight, cellWidth, cell, draw, solution)
    image.show()


if __name__ == '__main__':
    pass