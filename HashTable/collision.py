class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash_v = 0
        for c in key:
            hash_v += ord(c)
        return hash_v % self.MAX

    def __getitem__(self, item):
        hash_value = self.get_hash(item)
        if not self.arr[hash_value]:
            return
        for idx, element in enumerate(self.arr[hash_value]):
            if element[0] == item:
                return element[1]

    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        found = False
        for i, element in enumerate(self.arr[hash_value]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_value][i] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash_value].append((key, value))


if __name__ == "__main__":
    t = HashTable()

    t["march 9"] = 123
    t["march 9"] = 234
    t["march 6"] = 78
    t["march 17"] = 459
    print(t["march 6"])
