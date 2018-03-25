from random import randint
from solution import greedy, opt2

def print_graph(graph):
    for row in graph:
        print(row)

def generate_full_graph(size):
    graph = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(i, size):
            if i == j:
                graph[i][j] = 0
            else:
                rand = (randint(1, 20))
                graph[i][j] = graph[j][i] = rand
    return graph


if __name__ == '__main__':
    graph = generate_full_graph(10)
    print_graph(graph)
    path, weight = greedy(graph)
    print((path, weight))
    print(opt2(graph, path, weight))
