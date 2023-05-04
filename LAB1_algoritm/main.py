from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left =self.right= None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.size += 1

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value < node.value:
                node.left = self._insert(node.left, value)
            else:
                node.right = self._insert(node.right, value)
        return node

    def remove(self, value):
        if self.root is None:
            return
        else:
            self.root, removed = self._remove(self.root, value)
            if removed:
                self.size -= 1

    def _remove(self, node, value):
        if node is None:
            return node, False
        elif value < node.value:
            node.left, removed = self._remove(node.left, value)
            return node, removed
        elif value > node.value:
            node.right, removed = self._remove(node.right, value)
            return node, removed
        else:
            if node.left is None and node.right is None:
                return None, True
            elif node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._get_min(node.right)
                node.value = successor.value
                node.right, _ = self._remove(node.right, successor.value)
                return node, True

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def show_wide_tree(self):
        if self.root is None:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(str(node.value))
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            print(" ".join(level))

if __name__ == "__main__":
    tree = BinaryTree()

    while True:
        print("1. Додати значення")
        print("2. Видалити значення")
        print("3. Вивід дерева")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print('---------')
            value = int(input("Введіть значення: "))
            tree.insert(value)
            print('---------')
        elif choice == "2":
            print('---------')
            value = int(input("Введіть значення: "))
            tree.remove(value)
            print('---------')
        elif choice == "3":
            print('---------')
            tree.show_wide_tree()
            print('---------')
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")






