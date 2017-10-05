import random


def rand(min,max):
    return random.randint(min,max)


def genRandArr(n,min,max):
    arr=[]
    while n >= 0:
        arr.append(rand(min, max))
        n -= 1
    return arr

def genSortedArr(n,min,max):
    arr = genRandArr(n, min, max)
    arr.sort()
    return arr
