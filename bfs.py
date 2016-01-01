from pythonds.basic import Queue
from pythonds.graphs import Graph
def bfs(g,start,searchKey):
    vertexQueue=Queue()
    start.setDistance(0)
    vertexQueue.enqueue(start)
    while (vertexQueue.size()>0):
        currentVertex=vertexQueue.dequeue()
        print currentVertex.getId()
        if(searchKey==currentVertex.getId()):
            print "distance is",currentVertex.getDistance()
            break
        for vertex in currentVertex.getConnections():
            if (vertex.getColor()=="white"):
                vertex.setColor("gray")
                print currentVertex.getDistance()
                vertex.setDistance(currentVertex.getDistance()+1)
                vertexQueue.enqueue(vertex)
        currentVertex.setColor("black")


