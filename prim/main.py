from math import inf as _
from prim import prim

graph = [
    [0, 7, _, 5, _, _, _],
    [7, 0, 8, 9, 7, _, _],
    [_, 8, 0, _, 5, _, _],
    [5, 9, _, 0, 15, 6, _],
    [_, 7, 5, 15, 0, 8, 9],
    [_, _, _, 6, 8, 0, 11],
    [_, _, _, _, 9, 11, 0],
]

if __name__ == '__main__':
    print(prim(graph))
