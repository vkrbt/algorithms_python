import random
import time as t


def rand(min_val, max_val):
    return random.randint(min_val, max_val)


def gen_rand_arr(n, min_val, max_val):
    arr = []
    while n:
        arr.append(rand(min_val, max_val))
        n -= 1
    return arr


def gen_sorted_arr(n, min_val, max_val):
    arr = gen_rand_arr(n, min_val, max_val)
    arr.sort()
    return arr


def time():
    return t.time() * 1000

