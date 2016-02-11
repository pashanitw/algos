from pythonds.trees import BinarySearchTree

class Result:
    def __init__(self,n=None,isAncestor=False):
        self.key=n
        self.isAncestor=isAncestor

def commonAnsHelper(root,p,q):
    if root==None:
        return None
    if root.key==p and root.key==q:
        return root.key
    l=commonAnsHelper(root.leftChild,p,q)
    r=commonAnsHelper(root.rightChild,p,q)
    if l!=None and r!=None:
        print l.key,r.key
        return Result(root.key,True)
    elif root.key==p or root.key==q:
            isAns=False
            if l or r:
                isAns=True
            return Result(root.key,isAns)
    else:
        if l:
            return l
        else:
            return r

def findLeastAncestor(root,p,q):
    ans=commonAnsHelper(root,p,q)
    if ans:
        if ans.isAncestor:
            return ans.key
        else: return False
    else:
        return False
while(True):
    tree=BinarySearchTree()
    user_input=input("enter tree data with comma separated values:")
    for i in user_input:
        tree.put(i,i)
    nodes=input("enter nodes to find ancestor")
    print findLeastAncestor(tree.root,nodes[0],nodes[1])
