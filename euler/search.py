def degree_of_vertex(row):
    return sum(row)

def get_vertex(row):
    return row.index(1)

def find_cycle(graph):
    stack = []
    stack.append(0)
    res = []
    while stack:
        current = stack[-1]
        if degree_of_vertex(graph[current]) == 0:
            stack.pop()
            res.append(current)
        else:
            vertex = get_vertex(graph[current])
            graph[vertex][current] = graph[current][vertex] = 0
            stack.append(vertex)
    return res
