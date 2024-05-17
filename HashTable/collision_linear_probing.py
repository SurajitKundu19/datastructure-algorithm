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
        if self.arr[hash_value] and self.arr[hash_value][0] == item:
            return self.arr[hash_value][1]
        if self.arr[hash_value]:
            pos_counter = hash_value + 1
            counter = 0
            while counter < self.MAX:
                if (
                    self.arr[pos_counter % self.MAX]
                    and self.arr[pos_counter % self.MAX][0] == item
                ):
                    return self.arr[pos_counter % self.MAX][1]
                    break
                counter += 1
                pos_counter += 1

    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        if not self.arr[hash_value] or (
            self.arr[hash_value] and self.arr[hash_value][0] == key
        ):
            self.arr[hash_value] = (key, value)
        else:
            pos_counter = hash_value + 1
            counter = 0
            while counter < self.MAX:
                if not self.arr[pos_counter % self.MAX]:
                    self.arr[pos_counter % self.MAX] = (key, value)
                    break
                counter += 1
                pos_counter += 1


if __name__ == "__main__":
    t = HashTable()

    t["march 9"] = 123
    t["march 9"] = 234
    t["march 6"] = 78
    t["march 17"] = 459
    print(t.arr)
    print(t["march 9"])
    print(t["march 17"])
    print(t["march 6"])
