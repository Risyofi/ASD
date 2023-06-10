"""
Muhammad Irfan Abidin / L200210021
"""
class Simpul(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data) + "->", end='')
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.data) + "->", end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data) + "->", end='')


a = Simpul("1")
b = Simpul("2")
c = Simpul("3")
d = Simpul("4")
e = Simpul("5")
f = Simpul("6")
g = Simpul("7")

a.left = b; a.right = c
b.left = d; b.right = e
c.left = f; c.right = g

print("Inorder traversal of the BST:")
inorder(a)
print()
print("\nPreorder traversal of the BST:")
preorder(a)
print()
print("\nPostorder traversal of the BST:")
postorder(a)
