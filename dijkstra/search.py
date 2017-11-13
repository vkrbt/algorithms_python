from collections import deque
from math import inf


def search(graph):
    verticesNumber = len(graph[0])
    lens = [inf] * verticesNumber
    used = [False] * verticesNumber

    vertices = range(verticesNumber)
    for i in vertices:
        v = None
        for j in vertices:
            if not used[j] and (v in None or lens[j] < lens[v]):
                v = j
        if lens[v] == inf:
            break
        used[v] = True
