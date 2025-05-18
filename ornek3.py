class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def print_tree(node, level=0, prefix="Root:"):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        print_tree(node.left, level + 1, prefix="L---")
        print_tree(node.right, level + 1, prefix="R---")

# Başlangıç dizisi
values = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# BST oluştur
root = None
for v in values:
    root = insert
