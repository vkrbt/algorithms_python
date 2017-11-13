from depth_first_search.labyrinth import generate
from depth_first_search.labyrinth.draw import draw, drawSolution
from depth_first_search.search.search import search

SIZE = 10

if __name__ == '__main__':
    labyrinth = generate(SIZE)
    solution = search(labyrinth, SIZE)

    drawSolution(labyrinth, solution, SIZE, 200)

