from breadth_first_search import isGraphClosed
from graph import closedGraph, unclosedGraph

if __name__ == '__main__':
    print(isGraphClosed(closedGraph))
    print(isGraphClosed(unclosedGraph))
