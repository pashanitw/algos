class BinaryTree:
    def __init__(self,objkey):
        self.key=objkey
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            temp=BinaryTree(newNode)
            temp.leftChild=self.leftChild
            self.leftChild=temp
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            temp=BinaryTree(newNode)
            temp.rightChild=self.rightChild
            self.rightChild=temp
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
'''
r=BinaryTree('a')
print (r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getLeftChild().getRootVal())
print(r.getRightChild().getRootVal())
'''
