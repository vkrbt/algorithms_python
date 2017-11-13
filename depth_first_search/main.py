from labyrinth.labyrinth import generate
from labyrinth.draw import draw, drawSolution
from search.search import search

SIZE = 10

if __name__ == '__main__':
    labyrinth = generate(SIZE)
    solution = search(labyrinth, SIZE)

    drawSolution(labyrinth, solution, SIZE, 400)

