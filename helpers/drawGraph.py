from PIL import Image, ImageDraw, ImageFont

def draw(graph=[]):
    image = Image.new('RGBA', (400, 400))
    draw = ImageDraw.Draw(image)
    drawCircle((200, 200), 200, draw)
    image.show()


def drawCircle(point, radius, draw, fill=(0, 0, 0), outline=(255,255, 255)):
    start = (point[0] - radius, point[1] - radius)
    end = (point[0] + radius - 1, point[1] + radius - 1)
    draw.ellipse((start, end), fill, outline)

if __name__ == '__main__':
    draw()
