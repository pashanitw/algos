class TreeNode:
    def __init__(self,key=None,parent=None,lc=None,rc=None):
        self.key=key
        self.leftChild=lc
        self.rightChild=rc
        self.parent=parent
        self.root=None
    def getKey(self):
        return  self.key
    def insert(self,key):
        if self.root:
            self.put(key,self)
        else:
            self.root=True
            self.key=key
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self
    def isRightChild(self):
        return self.parent and self.parent.rightChild==self
    def isLeaf(self):
        return (not self.leftChild) and (not self.rightChild)
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    def hasBothChildrens(self):
        return self.leftChild and self.rightChild
    def put(self,key,node):
        if(key<node.key):
            if(node.hasLeftChild()):
                self.put(key,node.leftChild)
            else:
                node.leftChild=TreeNode(key,node)
        else:
            if(node.hasRightChild()):
                self.put(key,node.rightChild)
            else:
                node.rightChild=TreeNode(key,node)
    def inOrder(self,node):
        if node==None:
            return
        print (node.key)
        self.inOrder(node.leftChild)
        self.inOrder(node.rightChild)
    def findNode(self,key,node):
        if(key==node.key or node==None):
            return node
        elif key<node.key:
           return self.findNode(key,node.leftChild)
        else:
           return self.findNode(key,node.rightChild)
    def replaceNodeData(self,key,left=None,right=None,parent=None):
        self.key=key
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self
    def findSuccessor(self,key):
        node=self.findNode(key,self)
        if node.hasRightChild():
            return self.findMin(node.rightChild)
        else:
            y=node.parent
            x=node
            while y and y.rightChild==x:
                x=y
                y=y.parent
            return y
    def findMin(self,node):
        if not node.hasLeftChild():
                return node
        return self.findMin(node.leftChild)

    def remove(self,key):
        node=self.findNode(key,self)
        if not node:
            print("did not find the node u removed")
        else:
            if node.isLeaf():
                parent=node.parent
                if node.isLeftChild():
                    parent.leftChild=None
                if node.isRightChild():
                    parent.rightChild=None
            if not node.hasBothChildrens():
                if node.hasLeftChild():
                    if node.isLeftChild():
                        parent=node.parent
                        child=node.leftChild
                        parent.leftChild=child
                        child.parent=parent
                    if node.isRightChild():
                        parent=node.parent
                        child=node.leftChild
                        parent.rightChild=child
                        child.parent=parent
                    else:
                        child=node.leftChild
                        self.replaceNodeData(child.key,child.leftChild,child.rightChild)
                if node.hasRightChild():
                    if node.isLeftChild():
                        parent=node.parent
                        child=node.rightChild
                        parent.leftChild=child
                        child.parent=parent
                    if node.isRightChild():
                        parent=node.parent
                        child=node.rightChild
                        parent.rightChild=child
                        child.parent=parent
                    else:
                        child=node.rightChild
                        self.replaceNodeData(child.key,child.leftChild,child.rightChild)
            if node.hasBothChildrens():
                
            else:
                print("fuck its not in any case")






tree=TreeNode()
tree.insert(17)
tree.insert(5)
tree.insert(2)
tree.insert(35)
tree.insert(11)
tree.insert(29)
tree.insert(38)
tree.insert(9)
tree.insert(1)
print tree.findSuccessor(5).key