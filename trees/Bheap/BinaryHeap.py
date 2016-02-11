class BinaryHeap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]>self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
    def insert(self,element):
        self.heapList.append(element)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)
    def percDown(self,i):
        while (i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]<self.heapList[mc]:
                tmp=self.heapList[mc]
                self.heapList[mc]=self.heapList[i]
                self.heapList[i]=tmp
            i=mc
    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delMin(self):
        delElem=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.percDown(1)
        return delElem
    def buildHeap(self,alist):
        self.heapList=[0]+alist[:]
        i=len(alist)
        i=i//2
        self.currentSize=i
        while (i>0):
            self.percDown(i)
            i=i-1
heap=BinaryHeap()
list=[7,2,5,1,5,1,12,32,41]
heap.buildHeap(list)
print heap.delMin()





