from Binary import BinaryTree

def findRootNode(tree,item):
    if tree==None:
        tree=BinaryTree(item)

    elif item<tree.getRootVal():
        tree.leftChild=findRootNode(tree.leftChild,item)
    else:
        tree.rightChild=findRootNode(tree.rightChild,item)
    return tree



def insertBsTree(list):
    tree=None
    for i in list:
        tree=findRootNode(tree,i)
    print ("tree is",tree)
    return tree

def inOrder(tree):
    if tree==None:
        return
    print (tree.getRootVal())
    inOrder(tree.getLeftChild())
    inOrder(tree.getRightChild())

def preOrder(tree):
    if(tree==None):
        return
    inOrder(tree.getLeftChild())
    print(tree.getRootVal())
    inOrder(tree.getRightChild())
def postOrder(tree):
    if tree==None:
        return
    postOrder(tree.getLeftChild())
    postOrder(tree.getRightChild())
    print (tree.getRootVal())
list=[5,4,6,7,10,11]
tree=insertBsTree(list)
postOrder(tree)