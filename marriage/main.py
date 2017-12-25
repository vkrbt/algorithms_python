from marriage import marriage

men = [[0, 1, 2], [2, 0, 1], [2, 1, 0]]

women = [[2, 1, 0], [1, 0, 2], [0, 2, 1]]

if __name__ == '__main__':
    print(marriage(men, women))
