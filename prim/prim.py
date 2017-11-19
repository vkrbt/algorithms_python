from math import isinf, inf

def prim(graph):
    minimalSpannigTree = []
    start = 0
    print(getMinConnectedEdge(graph, start, minimalSpannigTree))


def getMinConnectedEdge(graph, vertexPosition, spanningTree):
    row = graph[vertexPosition]
    vertices = []
    for vertex in range(len(row)):
        weight = row[vertex]
        if not isinf(weight) and weight != 0:
            vertices.append(vertex)
    minVertex = vertices[0]
    for vertex in vertices:
        print(vertex, row[vertex])
        if row[vertex] < row[minVertex]:
            minVertex = vertex
    print(minVertex)



