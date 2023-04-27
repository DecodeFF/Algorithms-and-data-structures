class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def insert(self, key, value):
        hash_value = self.hash_function(key)

        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                self.values[hash_value] = value  # update existing key
                return
            hash_value = self.rehash(hash_value)

        self.keys[hash_value] = key
        self.values[hash_value] = value

    def search(self, key):
        hash_value = self.hash_function(key)

        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                return self.values[hash_value]
            hash_value = self.rehash(hash_value)

        return None

    def delete(self, key):
        hash_value = self.hash_function(key)

        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                self.keys[hash_value] = None
                self.values[hash_value] = None
                return
            hash_value = self.rehash(hash_value)

    def display(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"[{self.keys[i]}, {self.values[i]}]", end="")
        print()


if __name__ == "__main__":
    size = int(input("Enter the size of hash table: "))
    hash_table = HashTable(size)
    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            hash_table.insert(key, value)
            hash_table.display()
        elif choice == 2:
            key = input("Enter key: ")
            value = hash_table.search(key)
            if value is not None:
                print(f"Value for key {key}: {value}")
            else:
                print(f"Key {key} not found")
        elif choice == 3:
            key = input("Enter key: ")
            hash_table.delete(key)
            hash_table.display()
        elif choice == 4:
            hash_table.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
