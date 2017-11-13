def find_cycle(graph):
    if is_euler(graph):
        stack = []
        stack.append(0)
        res = []
        while stack:
            current = stack[-1]
            if sum(graph[current]) == 0:
                res.append(stack.pop())
            else:
                vertex = graph[current].index(1)
                graph[vertex][current] = 0
                graph[current][vertex] = 0
                stack.append(vertex)
        return res
    else:
        return None


def is_euler(graph):
    for row in graph:
        if (sum(row) % 2) != 0:
            return False
    return True
