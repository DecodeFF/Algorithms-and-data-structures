# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def build_tree(nodes):
#     # Функція для побудови бінарного дерева зі списку вузлів
#     if not nodes:
#         return None
#     val = nodes.pop(0)
#     if val is None:
#         return None
#     node = TreeNode(val)
#     node.left = build_tree(nodes)
#     node.right = build_tree(nodes)
#     return node
#
# def inorder_traversal(root):
#     # Функція для обходу бінарного дерева в порядку inorder
#     if not root:
#         return []
#     res = []
#     res += inorder_traversal(root.left)
#     res.append(root.val)
#     res += inorder_traversal(root.right)
#     return res
#
# def preorder_traversal(root):
#     # Функція для обходу бінарного дерева в порядку preorder
#     if not root:
#         return []
#     res = []
#     res.append(root.val)
#     res += preorder_traversal(root.left)
#     res += preorder_traversal(root.right)
#     return res
#
# def postorder_traversal(root):
#     # Функція для обходу бінарного дерева в порядку postorder
#     if not root:
#         return []
#     res = []
#     res += postorder_traversal(root.left)
#     res += postorder_traversal(root.right)
#     res.append(root.val)
#     return res
#
# if __name__ == "__main__":
#     root = None
#     choice = '0'
#     while choice != '7':
#         print("Menu:")
#         print("1. Build tree;")
#         print("2. Inorder traversal;")
#         print("3. Preorder traversal;")
#         print("4. Postorder traversal;")
#         print("5. Exit;")
#         print("Input your choice:")
#         choice = input()
#         if choice == '1':
#             print("Input the values for nodes (separated by commas):")
#             nodes = input().split(',')
#             root = build_tree(nodes)
#             print("Tree built.")
#         elif choice == '2':
#             print("Inorder traversal:")
#             print(inorder_traversal(root))
#         elif choice == '3':
#             print("Preorder traversal:")
#             print(preorder_traversal(root))
#         elif choice == '4':
#             print("Postorder traversal:")
#             print(postorder_traversal(root))
#         elif choice == '5':
#             print("Exiting...")
#         else:
#             print("Invalid choice. Please try again.")






# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         if not self.root:
#             self.root = Node(value)
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, node):
#         if value < node.value:
#             if node.left is None:
#                 node.left = Node(value)
#             else:
#                 self._insert(value, node.left)
#         else:
#             if node.right is None:
#                 node.right = Node(value)
#             else:
#                 self._insert(value, node.right)
#
#     def search(self, value):
#         if self.root:
#             return self._search(value, self.root)
#         else:
#             return None
#
#     def _search(self, value, node):
#         if value == node.value:
#             return node
#         elif value < node.value and node.left is not None:
#             return self._search(value, node.left)
#         elif value > node.value and node.right is not None:
#             return self._search(value, node.right)
#
#     def delete(self, value):
#         if self.root is not None:
#             self.root = self._delete(value, self.root)
#
#     def _delete(self, value, node):
#         if value == node.value:
#             if node.left is None and node.right is None:
#                 return None
#             elif node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             else:
#                 tempNode = node.right
#                 while tempNode.left is not None:
#                     tempNode = tempNode.left
#
#                 node.value = tempNode.value
#                 node.right = self._delete(tempNode.value, node.right)
#
#         elif value < node.value:
#             node.left = self._delete(value, node.left)
#         elif value > node.value:
#             node.right = self._delete(value, node.right)
#
#         return node
#
#     def show(self):
#         if self.root:
#             self._show(self.root)
#
#     def _show(self, node):
#         if node is not None:
#             self._show(node.left)
#             print(node.value)
#             self._show(node.right)
#
# if __name__ == "__main__":
#     bst = BinarySearchTree()
#
#     while True:
#         print("\nBinary Search Tree Menu")
#         print("1. Insert value")
#         print("2. Search value")
#         print("3. Delete value")
#         print("4. Show tree")
#         print("5. Exit")
#
#         choice = int(input("Enter choice: "))
#
#         if choice == 1:
#             value = int(input("Enter value to insert: "))
#             bst.insert(value)
#         elif choice == 2:
#             value = int(input("Enter value to search: "))
#             node = bst.search(value)
#             if node:
#                 print(f"Value {node.value} found in the tree.")
#             else:
#                 print(f"Value {value} not found in the tree.")
#         elif choice == 3:
#             value = int(input("Enter value to delete: "))
#             bst.delete(value)
#         elif choice == 4:
#             bst.show()
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice. Please try again.")




#
# from collections import deque
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left =self.right= None
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def insert(self, value):
#         self.root = self._insert(self.root, value)
#         self.size += 1
#
#     def _insert(self, node, value):
#         if node is None:
#             return Node(value)
#         else:
#             if value < node.value:
#                 node.left = self._insert(node.left, value)
#             else:
#                 node.right = self._insert(node.right, value)
#         return node
#
#     def remove(self, value):
#         if self.root is None:
#             return
#         else:
#             self.root, removed = self._remove(self.root, value)
#             if removed:
#                 self.size -= 1
#
#     def _remove(self, node, value):
#         if node is None:
#             return node, False
#         elif value < node.value:
#             node.left, removed = self._remove(node.left, value)
#             return node, removed
#         elif value > node.value:
#             node.right, removed = self._remove(node.right, value)
#             return node, removed
#         else:
#             if node.left is None and node.right is None:
#                 return None, True
#             elif node.left is None:
#                 return node.right, True
#             elif node.right is None:
#                 return node.left, True
#             else:
#                 successor = self._get_min(node.right)
#                 node.value = successor.value
#                 node.right, _ = self._remove(node.right, successor.value)
#                 return node, True
#
#     def _get_min(self, node):
#         while node.left is not None:
#             node = node.left
#         return node
#
#     def dfs(self):
#         self._dfs(self.root)
#
#     def _dfs(self, node):
#         if node is None:
#             return
#         self._dfs(node.left)
#         print(node.value)
#         self._dfs(node.right)
#
#     def bfs(self):
#         if self.root is None:
#             return
#         queue = deque()
#         queue.append(self.root)
#         while queue:
#             node = queue.popleft()
#             print(node.value)
#             if node.left is not None:
#                 queue.append(node.left)
#             if node.right is not None:
#                 queue.append(node.right)
#
#     def show(self):
#         if self.root:
#             self._show(self.root)
#
#     def _show(self, node):
#         if node is not None:
#             self._show(node.left)
#             print(node.value)
#             self._show(node.right)
#
# if __name__ == "__main__":
#     tree = BinaryTree()
#
#     while True:
#         print("1. Додати значення")
#         print("2. Видалити значення")
#         print("3. Вивід дерева")
#         print("4. Обійти дерево (DFS)")
#         print("5. Обійти дерево (BFS)")
#         print("6. Вийти")
#
#         choice = input("Ваш вибір: ")
#
#         if choice == "1":
#             print('---------')
#             value = int(input("Введіть значення: "))
#             tree.insert(value)
#             print('---------')
#         elif choice == "2":
#             print('---------')
#             value = int(input("Введіть значення: "))
#             tree.remove(value)
#             print('---------')
#         elif choice == "3":
#             print('---------')
#             tree.show()
#             print('---------')
#         elif choice == "4":
#             print('---------')
#             print("Обхід дерева (DFS):")
#             tree.dfs()
#             print('---------')
#         elif choice == "5":
#             print('---------')
#             print("Обхід дерева (BFS):")
#             tree.bfs()
#             print('---------')
#         elif choice == "6":
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")




class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

            return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def show_wide_tree(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

#     def get_values(self, max_values):
#         values = []
#         count = 0
#         while count < max_values:
#             try:
#                 value = input("Введіть значення, або 'q' для виходу: ")
#                 if value == 'q':
#                     break
#                 value = int(value)
#                 values.append(value)
#                 count += 1
#             except ValueError:
#                 print("Неправильний формат значення. Спробуйте ще раз.")
#         return values
#
# if __name__ == "__main__":
#     t = Tree()
#     max_values=int(input("Ведіть макс значення:"))
#
#     choice = input("1. Додати значення\n2. Показати дерево\n3. Вихід\nВаш вибір: ")
#
#     if choice == "1":
#         values = t.get_values(max_values)
#         for value in values:
#             t.append(Node(value))
#     elif choice == "2":
#         t.show_wide_tree(t.root)
#     elif choice == "3":
#         pass  # Тут можна вийти з програми або зробити інше
#     else:
#         print("Невірний вибір")




v = [10,5,7,16,13,2,20]
t = Tree()
for x in v:
    t.append(Node(x))
t.del_node(3)
t.show_wide_tree(t.root)




