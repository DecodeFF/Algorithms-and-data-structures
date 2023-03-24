class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self.hash(key)
        self.table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self.hash(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_key = self.hash(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                return True
        return False

    def __str__(self):
        return '\n'.join(f'{i}: {bucket}' for i, bucket in enumerate(self.table))

ht = ChainedHashTable(5)
ht.insert(2, "Hello")
ht.insert(12, "World")
ht.insert(22, "Hash")
ht.insert(4, "Table")
print(ht.search(12))
print(ht.search(6))
ht.delete(22)
print(ht)
