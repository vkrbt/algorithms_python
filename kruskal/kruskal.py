from math import inf, isinf

def kruskal(graph):
    minimalSpanningTree = []
    marks = {}
    for mark in range(len(graph)):
        marks[mark] = mark
    while len(minimalSpanningTree) < len(graph) - 1:
        minEdge = getMinEdge(graph, marks)
        minimalSpanningTree.append(minEdge)
        marks = changeMarks(marks, marks[minEdge[0]], marks[minEdge[1]])
    return minimalSpanningTree

def getMinEdge(graph, marks):
    minEdge = inf
    edge = ();
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            cell = graph[i][j]
            if cell > 0 and cell < minEdge:
                if marks[i] != marks[j]:
                    minEdge = graph[i][j]
                    edge = (i, j)
    return edge

def changeMarks(marks, oldMark, newMark):
    for key in marks:
        if marks[key] == oldMark:
            marks[key] = newMark
    return marks

