def binary_search(sorted_array, item):
    min_index = 0
    max_index = len(sorted_array) - 1
    result = dict.fromkeys(['iteration', 'index'])
    result['iteration'] = 0
    result['index'] = -1
    while min_index <= max_index:
        result['iteration'] += 1
        middle = (max_index + min_index) // 2
        current = sorted_array[middle]
        if current == item:
            result['index'] = middle
            return result
        if item < current:
            max_index = middle - 1
        if item > current:
            min_index = middle + 1
    return result