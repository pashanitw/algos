import sys
sys.setrecursionlimit(1000000000)
from pythonds.graphs import Graph
g=Graph()
i=0
finishingTime=0
l={}
g1=Graph()
temp=[]
def myDfs(currentVertex):
    currentVertex.setColor("gray")
    for vertex in currentVertex.getConnections():
        if vertex.getColor()=="white":
            myDfs(vertex)
    currentVertex.setColor("black")
    temp.append(currentVertex.getId())
    return temp

def Dfs(currentVertex):
    global finishingTime
    currentVertex.setColor("gray")
    for vertex in currentVertex.getConnections():
        vertex.incomings.append(currentVertex)
        if vertex.getColor()=="white":
            Dfs(vertex)
    currentVertex.setColor("black")
    finishingTime+=1
    l[finishingTime]=currentVertex.getId()



def reverseEdges():
    for vertex in g.getVertices():
        currentVertex=g.getVertex(vertex)
        for incoming in currentVertex.incomings:
            g1.addEdge(currentVertex.getId(),incoming.getId())
maxLengths=[0,0,0,0,0]
def processMaxLengths(le):
    for counter in range(len(maxLengths)):
        if le>maxLengths[counter]:
            maxLengths[counter]=le
            break
def connectedComponents():
    for i in range(finishingTime,0,-1):
        vertId=l[i]
        if g1.getVertex(vertId).getColor()!="black":
            global temp
            temp=[]
            val=myDfs(g1.getVertex(vertId))
            if len(val)>1 :
                processMaxLengths(len(val))


'''
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(2,3)
g.addEdge(3,6)
g.addEdge(4,2)
g.addEdge(5,1)
g.addEdge(5,4)
g.addEdge(4,7)
g.addEdge(7,5)
g.addEdge(6,8)
g.addEdge(8,9)
g.addEdge(9,6)
'''
'''
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,3)
g.addEdge(5,1)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(7,6)
g.addEdge(3,7)
g.addEdge(8,7)
g.addEdge(4,8)
g.addEdge(8,4)

'''
wfile = open("SCC.txt",'r')

for line in wfile:
    str=line.strip()
    word=line[:-1].split()
    g.addEdge(word[0],word[1])


for vertex in g.getVertices():
    vert=g.getVertex(vertex)
    if(vert.getColor()!="black"):
        Dfs(vert)
reverseEdges()
connectedComponents()
print (maxLengths)
'''
for v in g1:
   for w in v.getConnections():
       print("( %s , %s )" % (v.getId(), w.getId()))
'''