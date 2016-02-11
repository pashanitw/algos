from pythonds.trees.bst import BinarySearchTree
from pythonds.trees.bst import TreeNode


def insertMinimalTree(tuple,start,end):
    if(start>end):
        return None
    mid=(start+end)/2
    root=TreeNode(tuple[mid],tuple[mid])
    root.leftChild=insertMinimalTree(tuple,start,mid-1)
    root.rightChild=insertMinimalTree(tuple,mid+1,end)
    return root

def inorder(tree):
    if tree != None:
        print tree.key
        inorder(tree.leftChild)
        inorder(tree.rightChild)

while(True):
    data=input("please enter comma separated values : ")
    inorder(insertMinimalTree(data,0,len(data)-1))