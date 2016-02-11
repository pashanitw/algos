
def findMin(root):
        if not root.hasLeftChild():
            return root
        return findMin(root.leftChild)
def findSuccessor(root):
    if root.hasRightChild():
        return findMin(root.rightChild)
    else:
        x=root
        y=x.parent
        while y and y.rightChild==x:
            x=y
            y=x.parent
        return y