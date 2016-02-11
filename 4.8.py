from pythonds.trees.bst import BinarySearchTree

def treeMatch(root,node):
    if root:
        if root.key!=node.key:
            print("match at",root.key,node.key)
            return False
    else:
        return True
    return treeMatch(root.leftChild,node.leftChild) and treeMatch(root.rightChild,node.rightChild)

def isSubtree(t1,t2):
    if (not t1) and (not t2):
        return True
    elif (not t1) or (not t2):
        return False
    else:
        loopSubTree(t1,t2)
def loopSubTree(t1,t2):
    if t1 and (t1.key==t2.key):
        if treeMatch(t2,t1):
            return True
        else:
            return False
    elif not t1:
        return False
    return loopSubTree(t1.leftChild,t2) or loopSubTree(t1.rightChild,t2)



while(True):
    tree1=BinarySearchTree()
    user_input=input("Enter Tree1 :")
    for i in user_input:
        tree1.put(i,i)
    tree2=BinarySearchTree()
    user_input=input("Enter Tree2 :")
    for i in user_input:
        tree2.put(i,i)
    print loopSubTree(tree1.root,tree2.root)


