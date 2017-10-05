def binarySearch(sortedArray, item):
    minIndex = 0
    maxIndex = len(sortedArray) - 1
    while minIndex <= maxIndex:
        middle = (maxIndex + minIndex) // 2
        current = sortedArray[middle]
        if current == item:
            return middle
        if item < current:
            maxIndex = middle - 1
        if item > current:
            minIndex = middle + 1
    return -1

def interpolationSort(sortedArray, item):
    minIndex = 0
    maxIndex = len(sortedArray) - 1
    while (minIndex <= maxIndex and
        sortedArray[minIndex] <= item <= sortedArray[maxIndex]):
        middle = minIndex + ((item - sortedArray[minIndex]) * (maxIndex - minIndex))\
                        // (sortedArray[maxIndex] - sortedArray[minIndex])
        current = sortedArray[middle]
        if current == item:
            return middle
        if item < current:
            maxIndex = middle - 1
        if item > current:
            minIndex = middle + 1
    return -1