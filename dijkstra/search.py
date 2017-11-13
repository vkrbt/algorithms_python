from collections import deque

def search(graph):
    lengths = {}
    lengths[0] = 0
    queue = deque()

    while queue:
        current = queue.pop()