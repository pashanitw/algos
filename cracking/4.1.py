from pythonds.trees.bst import BinarySearchTree
def inorder(tree):
    if tree != None:
        inorder(tree.leftChild)
        print tree.key
        inorder(tree.rightChild)

tree=BinarySearchTree()

#30,15,18,7,8,6,60,72
def height(tree):
    if tree==None:
        return -1
    else:
        return 1+max(height(tree.leftChild),height(tree.rightChild))
inorder(tree.root)

def isBalaanced(tree,done=False):
    if tree!=None:
            print ("visit",tree.key)
    rightHeight=False
    if(tree==None):
        return -1
    else:
       leftHeight=isBalaanced(tree.leftChild)
       print(leftHeight)
       if (type(leftHeight)==int):
           rightHeight=isBalaanced(tree.rightChild)
       val1=False
       val2=False
       if(type(leftHeight)==int):
           val1=True
       if(type(rightHeight)==int):
           val2=True

       if not(val1 and val2):
           print val1,val2
           return  False
       if abs(leftHeight-rightHeight)>1:
           print ("fuck shit")
           return False
       else:
           return 1+max(leftHeight,rightHeight)


user_input=input("enter tree data with comma separated values:")
for i in user_input:
    tree.put(i,i)
print isBalaanced(tree.root)