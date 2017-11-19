from math import inf
from kruskal import kruskal


graph = [
    [0, 7, inf, 5, inf, inf, inf],
    [7, 0, 8, 9, 7,inf, inf],
    [inf, 8, 0, inf, 5, inf, inf],
    [5, 9, inf, 0, 15, 6, inf],
    [inf, 7, 5, 15, 0, 8, 9],
    [inf, inf, inf, 6, 8, 0, 11],
    [inf, inf, inf, inf, 9, 11, 0],
]

if __name__ == '__main__':
    print(kruskal(graph))
