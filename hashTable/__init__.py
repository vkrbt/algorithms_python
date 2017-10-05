import json

HASH_CONSTANT = 103


def hash_function(value):
    return value % HASH_CONSTANT


class HashTable:
    values = {}

    def add(self, number):
        key = hash_function(number)
        if key in self.values.keys():
            self.values[key].append(number)
        else:
            self.values[key] = [number]

    def remove(self, number):
        key = hash(number)
        if key in self.values.keys() and number in self.values[key]:
            self.values[key].pop(self.values[key].index(number))
            if not len(self.values[key]):
                self.values.pop(key)

    def find(self, number):
        key = hash(number)
        if key in self.values.keys() and number in self.values[key]:
            return self.values[key][self.values[key].index(number)]
        else:
            raise ValueError('Could not find value.')

    def __str__(self):
        return json.dumps(self.values)


if __name__ == '__main__':
    hashTable = HashTable()

    hashTable.add(5)
    hashTable.add(108)
    hashTable.add(6)
    hashTable.remove(6)






