from marriage import marriage, Preferences

men = {
    'a': Preferences('a', ['A', 'B', 'C']),
    'b': Preferences('b', ['C', 'A', 'B']),
    'c': Preferences('c', ['C', 'B', 'A']),
}

women = {
    'A': Preferences('A', ['c', 'a', 'b']),
    'B': Preferences('B', ['b', 'a', 'c']),
    'C': Preferences('C', ['a', 'c', 'b']),
}

if __name__ == '__main__':
    for pair in marriage(men, women).values():
        print(pair)

