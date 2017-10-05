import search, helpers, timeit

TIMES = 10000000
NUM_TO_FIND = 31104

arr = helpers.genSortedArr(TIMES, 0, TIMES)

binTime = timeit.timeit()
binIndex = search.binarySearch(arr, NUM_TO_FIND)
binTime = timeit.timeit() - binTime

interTime = timeit.timeit()
interIndex = search.interpolationSort(arr, NUM_TO_FIND)
interTime = timeit.timeit() - interTime

print('Binary search time:', binTime)
print('Interpolation search time:', interTime)
print('Interpolation search faster:', binTime - interTime)
