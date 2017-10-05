HASH_CONSTANT = 103


def hash(value):
    return value % HASH_CONSTANT


class HashTable:
    values = {}

    def add(self, number):
        key = hash(number)
        if key in self.values.keys():
            self.values[key].append(number)
        else:
            self.values[key] = [number]
        print(self.values)

    def remove(self, number):
        key = hash(number)
        if key in self.values.keys() and number in self.values[key]:
            self.values[key].pop(self.values[key].index(number))
            if not len(self.values[key]):
                self.values.pop(key)
        print(self.values)

    def find(self, number):
        key = hash(number)
        if key in self.values.keys() and number in self.values[key]:
            return self.values[key][self.values[key].index(number)]
        else:
            raise ValueError('Could not find value.')


hashTable = HashTable()

hashTable.add(5)
hashTable.add(108)
hashTable.add(6)
hashTable.remove(6)






