def binary_search(sorted_array, item):
    min_index = 0
    max_index = len(sorted_array) - 1
    while min_index <= max_index:
        middle = (max_index + min_index) // 2
        current = sorted_array[middle]
        if current == item:
            return middle
        if item < current:
            max_index = middle - 1
        if item > current:
            min_index = middle + 1
    return -1


def interpolation_search(sorted_array, item):
    min_index = 0
    max_index = len(sorted_array) - 1
    while (min_index <= max_index and
            sorted_array[min_index] <= item <= sorted_array[max_index]):
        middle = min_index + ((item - sorted_array[min_index]) * (max_index - min_index))\
                        // (sorted_array[max_index] - sorted_array[min_index])
        current = sorted_array[middle]
        if current == item:
            return middle
        if item < current:
            max_index = middle - 1
        if item > current:
            min_index = middle + 1
    return -1
