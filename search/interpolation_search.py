def interpolation_search(sorted_array, item):
    min_index = 0
    max_index = len(sorted_array) - 1
    result = dict.fromkeys(['iteration', 'index'])
    result['iteration'] = 0
    result['index'] = -1
    while (min_index <= max_index and
            sorted_array[min_index] <= item <= sorted_array[max_index]):
        result['iteration'] += 1
        middle = min_index + ((item - sorted_array[min_index]) * (max_index - min_index))\
                        // (sorted_array[max_index] - sorted_array[min_index])
        current = sorted_array[middle]
        if current == item:
            result['index'] = middle
            return result
        if item < current:
            max_index = middle - 1
        if item > current:
            min_index = middle + 1
    return result
