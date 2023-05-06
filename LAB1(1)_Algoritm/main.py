# Визначення структури вузла дерева
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


# Функція для додавання вузла в дерево
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


# Префіксний порядок обходу
def prefix_order(root):
    if root:
        print(root.val),
        prefix_order(root.left)
        prefix_order(root.right)


# Постфіксний порядок обходу
def postfix_order(root):
    if root:
        postfix_order(root.left)
        postfix_order(root.right)
        print(root.val),


# Інфіксний порядок обходу
def infix_order(root):
    if root:
        infix_order(root.left)
        print(root.val),
        infix_order(root.right)


# Приклад використання
if __name__ == '__main__':
    root = Node(5)
    insert(root, Node(3))
    insert(root, Node(7))
    insert(root, Node(1))
    insert(root, Node(9))

    print("Prefix Order :")
    prefix_order(root)
    print("\nPostfix Order :")
    postfix_order(root)
    print("\nInfix Order :")
    infix_order(root)
