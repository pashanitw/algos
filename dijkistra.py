from pythonds.graphs import PriorityQueue,Graph,Vertex
import sys

def Diskistra(startVertex,Graph):
    pq=PriorityQueue()
    for vertex in Graph:
        vertex.setDistance(sys.maxsize)
        vertex.setPred(None)
    startVertex.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in Graph])
    while not pq.isEmpty():
        currentVertex=pq.delMin()
        for vertex in currentVertex.getConnections():
            newCost=currentVertex.getDistance()+currentVertex.getWeight(vertex)
            if newCost<vertex.getDistance():
                vertex.setDistance(newCost)
                vertex.setPred(currentVertex)
                pq.decreaseKey(vertex,newCost)

G=Graph()
G.addEdge("u","v",2)
G.addEdge("v","u",2)
G.addEdge("v","w",3)
G.addEdge("w","v",3)
G.addEdge("u","w",5)
G.addEdge("w","u",5)
G.addEdge("u","x",1)
G.addEdge("x","u",1)
G.addEdge("x","v",2)
G.addEdge("v","x",2)
G.addEdge("x","v",2)
G.addEdge("x","w",3)
G.addEdge("w","x",3)
'''
G.addEdge("x","y",1)
G.addEdge("y","x",1)
G.addEdge("w","y",1)
G.addEdge("y","w",1)
G.addEdge("y","z",1)
G.addEdge("z","y",1)
'''
G.addEdge("w","z",5)
G.addEdge("z","w",5)



Diskistra(G.getVertex("u"),G)

for v in G:
    print ("( %s , %d)" % (v.getId(),v.getDistance()))