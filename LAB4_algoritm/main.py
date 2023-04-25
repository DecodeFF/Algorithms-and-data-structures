# # class ChainedHashTable:
# #     def __init__(self, size):
# #         self.size = size
# #         self.table = [[] for _ in range(size)]
# #
# #     def hash(self, key):
# #         return key % self.size
# #
# #     def insert(self, key, value):
# #         hash_key = self.hash(key)
# #         self.table[hash_key].append((key, value))
# #
# #     def search(self, key):
# #         hash_key = self.hash(key)
# #         for k, v in self.table[hash_key]:
# #             if k == key:
# #                 return v
# #         return None
# #
# #     def delete(self, key):
# #         hash_key = self.hash(key)
# #         for i, (k, v) in enumerate(self.table[hash_key]):
# #             if k == key:
# #                 del self.table[hash_key][i]
# #                 return True
# #         return False
# #
# #     def __str__(self):
# #         return '\n'.join(f'{i}: {bucket}' for i, bucket in enumerate(self.table))
# #
# # ht = ChainedHashTable(5)
# # ht.insert(2, "Hello")
# # ht.insert(12, "World")
# # ht.insert(22, "Hash")
# # ht.insert(4, "Table")
# # print(ht.search(12))
# # print(ht.search(6))
# # ht.delete(22)
# # print(ht)
#
#
# import math
#
# class Set:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data
#
# class HashTable:
#     def __init__(self):
#         self.capacity = 10
#         self.size = 0
#         self.array = [None] * self.capacity
#
#     def hashFunction(self, key):
#         return (key % self.capacity)
#
#     def checkPrime(self, n):
#         if n == 1 or n == 0:
#             return False
#         for i in range(2, int(math.sqrt(n))+1):
#             if n % i == 0:
#                 return False
#         return True
#
#     def getPrime(self, n):
#         if n % 2 == 0:
#             n += 1
#         while not self.checkPrime(n):
#             n += 2
#         return n
#
#     def init_array(self):
#         self.capacity = self.getPrime(self.capacity)
#         self.array = [None] * self.capacity
#
#     def insert(self, key, data):
#         index = self.hashFunction(key)
#         if self.array[index] is None:
#             self.array[index] = Set(key, data)
#             self.size += 1
#             print(f"Ключ ({key}) вставлен")
#         elif self.array[index].key == key:
#             self.array[index].data = data
#         else:
#             print("Возникла коллизия")
#
#     def remove_element(self, key):
#         index = self.hashFunction(key)
#         if self.array[index] is None:
#             print("Данного ключа не существует")
#         else:
#             self.array[index] = None
#             self.size -= 1
#             print(f"Ключ ({key}) удален")
#
#     def display(self):
#         for i in range(self.capacity):
#             if self.array[i] is None:
#                 print(f"array[{i}]: /")
#             else:
#                 print(f"Ключ: {self.array[i].key} array[{i}]: {self.array[i].data}\t")
#
#     def size_of_hashtable(self):
#         return self.size
#
# if __name__ == '__main__':
#     hashtable = HashTable()
#
#     while True:
#         print("1.Вставить элемент в хэш-таблицу")
#         print("2.Удалить элемент из хэш-таблицы")
#         print("3.Узнать размер хэш-таблицы")
#         print("4.Вывести хэш-таблицу")
#         choice = int(input("Пожалуйста, выберите нужный вариант: "))
#
#         if choice == 1:
#             key = int(input("Введите ключ: "))
#             data = int(input("Введите данные: "))
#             hashtable.insert(key, data)
#         elif choice == 2:
#             key = int(input("Введите ключ, который хотите удалить: "))
#             hashtable.remove_element(key)
#         elif choice == 3:
#             n = hashtable.size_of_hashtable()
#             print(f"Размер хэш-таблицы: {n}")
#         elif choice == 4:
#             hashtable.display()
#         else:
#             print("Неверно введены данные")
#
#         c = int(input("Продолжить? (Нажмите 1, если да): "))
#         if c != 1:
#             break

# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [None] * size
#
#     def hash_function(self, key):
#         hash_value = 0
#         for char in key:
#             hash_value += ord(char)
#         return hash_value % self.size
#
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         if self.table[index] is None:
#             self.table[index] = Node(key, value)
#         else:
#             current_node = self.table[index]
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = Node(key, value)
#
#     def search(self, key):
#         index = self.hash_function(key)
#         current_node = self.table[index]
#         while current_node is not None:
#             if current_node.key == key:
#                 return current_node.value
#             current_node = current_node.next
#         return None
#
#     def delete(self, key):
#         index = self.hash_function(key)
#         current_node = self.table[index]
#         previous_node = None
#         while current_node is not None:
#             if current_node.key == key:
#                 if previous_node is None:
#                     self.table[index] = current_node.next
#                 else:
#                     previous_node.next = current_node.next
#                 return
#             previous_node = current_node
#             current_node = current_node.next
#
#     def display(self):
#         for i in range(self.size):
#             print(f"{i}: ", end="")
#             current_node = self.table[i]
#             while current_node is not None:
#                 print(f"[{current_node.key}, {current_node.value}] -> ", end="")
#                 current_node = current_node.next
#             print()
#
#
# if __name__ == "__main__":
#     size = int(input("Enter the size of hash table: "))
#     hash_table = HashTable(size)
#     while True:
#         print("\n1. Insert")
#         print("2. Search")
#         print("3. Delete")
#         print("4. Display")
#         print("5. Exit")
#         choice = int(input("Enter your choice: "))
#         if choice == 1:
#             key = input("Enter key: ")
#             value = input("Enter value: ")
#             hash_table.insert(key, value)
#             hash_table.display()
#         elif choice == 2:
#             key = input("Enter key: ")
#             value = hash_table.search(key)
#             if value is not None:
#                 print(f"Value for key {key}: {value}")
#             else:
#                 print(f"Key {key} not found")
#         elif choice == 3:
#             key = input("Enter key: ")
#             hash_table.delete(key)
#             hash_table.display()
#         elif choice == 4:
#             hash_table.display()
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice")


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
