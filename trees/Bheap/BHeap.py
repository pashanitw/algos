class Bheap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def percUp(self,i):
        while i>=0:
            parent=i//2
            if(self.heapList[parent]>self.heapList[i]):
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[parent]
                self.heapList[parent]=tmp
    def percDown(self,i):
        while i*2<=self.currentSize:
            mc=i*2
            if(i*2+1 <= self.currentSize):
                if (self.heapList[i*2]>self.heapList[i*2+1]):
                    mc=i*2+1
            if(self.heapList[i]>self.heapList[mc]):
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc
    def insert(self,item):
        self.heapList.append(item)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)
    def deleteMin(self):
        item=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.percDown(1)
        return item
    def buildHeap(self,list):
        i=len(list)//2
        self.heapList=[0]+list[:]
        self.currentSize=len(list)
        while(i>0):
            self.percDown(i)
            i=i-1
        print (self.heapList)
heap=Bheap()
heap.buildHeap([9,3,5,2,6,7,1,4])
print(heap.deleteMin())
print(heap.deleteMin())
print(heap.deleteMin())
print(heap.deleteMin())
print(heap.deleteMin())
print(heap.deleteMin())

