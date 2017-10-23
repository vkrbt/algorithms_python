from collections import deque
from breadth_first_search import graph


def search(graph, start_point, end_point):
    search_queue = deque()
    search_queue += graph.get(str(start_point))
    searched = set()
    ancestors = {}
    for to in graph.get(str(start_point)):
        ancestors[to] = start_point
    found = False
    while search_queue and not found:
        point = search_queue.popleft()
        print(ancestors)
        if point not in searched:
            if point == end_point:
                found = True
                break
            else:
                for to in graph.get(str(point)):
                    ancestors[to] = point
                search_queue += graph.get(str(point))
                searched.add(point)
    path = []
    end = end_point
    while start_point not in path:
        path.append(end)
        end = ancestors.get(end)
    return path



if __name__ == '__main__':
    print(search(graph.graph, 0, 4))
