class TreeNode:
    def __init__(self,key,parent=None,lc=None,rc=None):
        self.key=key
        self.leftChild=lc
        self.rightChild=rc
        self.parent=parent
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
        return self.parent.leftChild==self
    def isRightChild(self):
        return self.parent.rightChild==self
    def isLeaf(self):
        return (not self.leftChild) and (not self.rightChild)
    def put(self,key,node):
        if(key<self.key):
            if(node.hasLeftChild()):
                self.put(key,self.leftChild)
            else:
                self.leftChild=TreeNode(key,node)
        else:
            if(node.hasRightChild()):
                self.put(key,self.rightChild)
            else:
                self.rightChild=TreeNode(key,node)

tree=TreeNode()
tree.insert(17)
tree.insert(5)
tree.insert(35)