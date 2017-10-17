import random
import time as t
import json
import os


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

FILENAME = os.path.abspath('./helpers/arrs.json')

def gen_arr_in_file(n, len):
    arr = []
    while n:
        arr.append(gen_sorted_arr(len, 0, len))
        n -= 1
    file = open(FILENAME, 'w')
    json.dump(arr, file)
    file.close()

def read_arrs_from_file():
    file = open(FILENAME, 'r')
    arr = json.load(file)
    return arr

if __name__ == '__main__':
    gen_arr_in_file(20, 1000000)
    read_arrs_from_file()