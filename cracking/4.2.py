from pythonds.graphs import Graph
from pythonds.basic import Queue

def pathExists(start,end):
    vertexQueue=Queue()
    vertexQueue.enqueue(start)
    while (vertexQueue.size()>0):
        item=vertexQueue.dequeue()
        if item.getId()==end.getId():
            print ("path exists")
            return True
        else:
            for vertex in item.getConnections():
                if vertex.getColor()=="white":
                    vertex.setColor("gray")
                    vertexQueue.enqueue(vertex)
    return False

g=Graph()
data=True
while data!=1000:
    data=input("enter tuple")
    if data!=1000:
        g.addEdge(data[0],data[1])
while(True):
    tuple=input("Please enter tuple u want to know the path")
    print pathExists(g.getVertex(tuple[0]),g.getVertex(tuple[1]))
    for vertex in g.getVertices():
        g.getVertex(vertex).setColor("white")


