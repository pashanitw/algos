# binary tree or not
from pythonds.trees.binaryTree import BinaryTree
prev=None
def isBinarySearchTree(root):
    global prev
    if root:
        if not isBinarySearchTree(root.leftChild):
            return False
        if (prev and prev.key>root.key):
            return False
        prev=root
        if not isBinarySearchTree(root.rightChild):
            return False
    return True

tree=BinaryTree(4)
tree.insertLeft(2)
tree.insertRight(5)
ls=tree.getLeftChild()
ls.insertLeft(1)
ls.insertRight(3)
print isBinarySearchTree(tree)


