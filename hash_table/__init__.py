import json
from random import randint

HASH_CONSTANT = 103


def hash_function(value):
    return value % HASH_CONSTANT


class HashTable:
    values = {}

    def add(self, number):
        key = hash_function(number)
        if key in self.values.keys():
            if number not in self.values[key]:
                self.values[key].append(number)
        else:
            self.values[key] = [number]

    def remove(self, number):
        key = hash_function(number)
        if key in self.values.keys() and number in self.values[key]:
            self.values[key].pop(self.values[key].index(number))
            if not len(self.values[key]):
                self.values.pop(key)
        else:
            raise ValueError('Item is not exist.')

    def find(self, number):
        key = hash_function(number)
        if key in self.values.keys() and number in self.values[key]:
            return self.values[key][self.values[key].index(number)]
        else:
            raise ValueError('Could not find value.')

    def __str__(self):
        keys = sorted(self.values.keys())
        return ''.join([str(key) + ': ' + json.dumps(self.values[key]) + '\n' for key in keys])


if __name__ == '__main__':
    hashTable = HashTable()

    for i in range(0, 1000):
        hashTable.add(randint(0, 100000))
    hashTable.add(350)
    print(hashTable.find(350))
    hashTable.remove(350)

    try:
        print(hashTable.find(350))
    except ValueError:
        print('Could not find value.')

    print(hashTable)







