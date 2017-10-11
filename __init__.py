from search import binary_search, interpolation_search
import helpers

ARR_LENGTH = 10000000
NUM_TO_FIND = 8*6*1*9*9*8
TIMES = 10000

arr = helpers.gen_sorted_arr(ARR_LENGTH, 0, TIMES)

# Binary search time executing.

times = TIMES
binTime = helpers.time()

while times:
    binary_search(arr, NUM_TO_FIND)
    times -= 1

binTime = helpers.time() - binTime

# Interpolation search time executing.

times = TIMES
interTime = helpers.time()

while times:
    interIndex = interpolation_search(arr, NUM_TO_FIND)
    times -= 1

interTime = helpers.time() - interTime

print('Binary search time:', binTime)
print('Interpolation search time:', interTime)
print('Interpolation search faster:', binTime - interTime)
