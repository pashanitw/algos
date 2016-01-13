from pythonds.graphs import Graph
from pythonds.basic import Queue
queue=Queue()
graph=Graph();
start=graph.addVertex("0,0")

def extractQuantity(quantities):
    quants=quantities.split(",")
    return [int(quants[0]),int(quants[1])]

def makeVertex(list):
    newList=[str(list[0]),str(list[1])]
    return ",".join(newList)

def findPossibleChildrens(vertex,q1,q2):
    childrens=[]
    quantities=extractQuantity(vertex.getId())
    quant1=quantities[0]
    quant2=quantities[1]
    # first quantity to river
    if not quant1==0:
        childrens.append(makeVertex([0,quant2]))
        if not quant2==q2:
            canHold=q2-quant2
            if(canHold>=quant1):
                temp2=quant2+quant1
                temp1=0
            else:
                temp2=canHold
                temp1=abs(canHold-quant1)
            childrens.append(makeVertex([temp1,temp2]))

    if not quant2==0:
        childrens.append(makeVertex([quant1,0]))
        if not quant1==q1:
            canHold=q1-quant1
            if(canHold>=quant2):
                temp1=quant2+quant1
                temp2=0
            else:
                temp1=canHold
                temp2=abs(canHold-quant2)
            childrens.append(makeVertex([temp1,temp2]))

    if quant1==0:
        temp1=q1
        childrens.append(makeVertex([temp1,quant2]))
    if quant2==0:
        temp2=q2
        childrens.append(makeVertex([quant1,temp2]))

    return childrens

def getPouringSteps(vertex,jug1,jug2,desired):
    vertex.setColor("gray")
    queue.enqueue(vertex)
    found=False
    while (queue.size()>0) & (not found):
        vert=queue.dequeue()
        node=extractQuantity(vert.getId())
        if (node[0]==desired) | (node[1]==desired):
             found=True
             print "count is",printPred(vert)
             #print node[0],node[1]

        childs=findPossibleChildrens(vert,jug1,jug2)
        for child in childs:
            if not child in graph:
                temp=graph.addVertex(child)
                temp.setPred(vert)
                queue.enqueue(temp)

def printPred(vertex):
    pred=vertex.getPred()
    if(pred):
        return printPred(pred)+1
    else:
        return 0
   # print extractQuantity(vertex.getId())


getPouringSteps(start,7,10,9)
getPouringSteps(start,5,11,10)
getPouringSteps(start,5,11,4)
getPouringSteps(start,5,11,3)
#childs=findPossibleChildrens(start)

#print childs