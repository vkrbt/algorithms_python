from math import inf

graph = {
    0: [0,   4,   10,   inf, inf, inf, inf],
    1: [inf, 0,   inf,  inf, 21,  inf, inf],
    2: [inf, inf, 0,    5,   inf, 8,   inf],
    3: [inf, inf, inf,  0,   5,   inf, inf],
    4: [inf, inf, inf,  inf, 0,   inf, 4],
    5: [inf, inf, inf,  inf, 12,  0,   inf],
    6: [inf, inf, inf,  inf, inf, inf, 0],
}

if __name__ == '__main__':
    print(9999<inf)