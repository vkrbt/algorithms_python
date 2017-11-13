from collections import deque

def isGraphClosed(graph):
    itemsToSearch = deque()

    firstKey = next(iter(graph.keys()))
    itemsToSearch += graph[firstKey]

    searched = set()
    searched.add(firstKey)
    while itemsToSearch:
        current = itemsToSearch.popleft()
        if current not in searched:
            searched.add(current)
            itemsToSearch += graph[current]

    return len(searched) == len(graph)
