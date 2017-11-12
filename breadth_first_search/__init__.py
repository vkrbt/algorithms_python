from collections import deque
from breadth_first_search.graph import closedGraph, unclosedGraph

def isGraphClosed(graph):
    itemsToSearch = deque()

    firstKey = next(iter(closedGraph.keys()))
    itemsToSearch += graph[firstKey]

    searched = set()
    searched.add(firstKey)
    while itemsToSearch:
        current = itemsToSearch.popleft()
        if current not in searched:
            searched.add(current)
            itemsToSearch += graph[current]

    return len(searched) == len(graph)


if __name__ == '__main__':
    print(isGraphClosed(closedGraph))
    print(isGraphClosed(unclosedGraph))