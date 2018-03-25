def get_next_nearest(graph, path):
    prev_point_pos = path[-1]
    next_point_pos = None
    next_point_weight = 999

    for i in range(len(graph[prev_point_pos])):
        point_weight = graph[prev_point_pos][i]
        if i != prev_point_pos and point_weight < next_point_weight and i not in path:
            next_point_pos = i
            next_point_weight = point_weight
    return next_point_pos, next_point_weight


def get_path_weight(graph, path):
    weight = 0
    prev_point = path[0]
    for i in range(1, len(path)):
        weight += graph[prev_point][path[i]]
        prev_point = path[i]
    weight += graph[path[0]][path[-1]]
    return weight


def greedy(graph):
    path = [0]
    weight = 0
    for _ in range(len(graph) - 1):
        next_pos, next_wight = get_next_nearest(graph, path)
        weight += next_wight
        path.append(next_pos)
    weight += graph[0][path[-1]]
    print(weight)
    print(get_path_weight(graph, path))
    return path, weight


def revese_path(path, pos1, pos2):
    path_part = path[pos1:pos2]
    path_part.reverse()
    return path[0:pos1] + path_part + path[pos2:]


def opt2(graph, path, weight):
    for i in range(1, len(path) - 3):
        for j in range(i + 2, len(path)):
            reversed_path = revese_path(path, i, j)
            reversed_path_weight = get_path_weight(graph, reversed_path)
            if reversed_path_weight < weight:
                path, weight = opt2(graph, reversed_path, reversed_path_weight)
    return path, weight
