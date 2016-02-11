##Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D,you'll have D linked lists).
from pythonds.trees.bst import TreeNode,BinarySearchTree
def listAtDepth(tree):
         list=[]
         root=tree.root
         temp=[root]
         while len(temp)>0:
             ls=[]
             list.append(temp)
             for node in temp:
                 if node.hasLeftChild():
                     ls.append(node.leftChild)
                 if node .hasRightChild():
                     ls.append(node.rightChild)
             temp=ls
         return list

while(True):
    tree=BinarySearchTree()
    data=input("please enter tree data : ")
    for item in data:
        tree.put(item,item)
    tree.preorder()
    print("level order")
    for level in listAtDepth(tree):
        for item in level:
            print item.key
        print ("new level")
