from depth_first_search.labyrinth.labyrinth import generate, SIZE
from depth_first_search.labyrinth.draw import draw

if __name__ == '__main__':
    draw(generate(), SIZE, SIZE)
