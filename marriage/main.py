from marriage import marriage

men = {
    'a': ['A', 'B', 'C'],
    'b': ['C', 'A', 'B'],
    'c': ['C', 'B', 'A'],
}

women = {
    'A': ['c', 'a', 'b'],
    'B': ['b', 'a', 'c'],
    'C': ['a', 'c', 'b'],
}

if __name__ == '__main__':
    marriage(men, women)

