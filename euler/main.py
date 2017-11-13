from search import find_cycle, is_euler

with_cycle1 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
]

with_cycle = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]

without_cycle = [
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
]

if __name__ == '__main__':
    print(is_euler(with_cycle1))
    print(find_cycle(with_cycle1))
    print(is_euler(with_cycle))
    print(find_cycle(with_cycle))
    print(is_euler(without_cycle))
    print(find_cycle(without_cycle))