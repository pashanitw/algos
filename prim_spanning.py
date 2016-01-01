from pythonds.graphs import PriorityQueue,Graph,Vertex
import sys

def prim(startVertex,Graph):
    pq=PriorityQueue()
    for vertex in Graph:
        vertex.setDistance(sys.maxsize)
        vertex.setPred(None)
    startVertex.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in Graph])
    while not pq.isEmpty():
        currentVertex=pq.delMin()
        pred=currentVertex.getPred()
        if pred:
            print ("( %s ,%s , %d)" % (currentVertex.getId(),pred.getId(),currentVertex.getDistance()))
        print currentVertex.getId(),
        for vertex in currentVertex.getConnections():
            newCost=currentVertex.getWeight(vertex)
            if newCost<vertex.getDistance():
                vertex.setDistance(newCost)
                vertex.setPred(currentVertex)
                pq.decreaseKey(vertex,newCost)


G=Graph()
G.addEdge("a","b",2)
G.addEdge("b","a",2)
G.addEdge("a","c",3)
G.addEdge("c","a",3)
G.addEdge("b","c",1)
G.addEdge("c","b",1)
G.addEdge("b","d",1)
G.addEdge("d","b",1)
G.addEdge("b","e",4)
G.addEdge("e","b",4)
G.addEdge("d","e",1)
G.addEdge("e","d",1)
G.addEdge("c","f",5)
G.addEdge("f","c",5)
G.addEdge("e","f",1)
G.addEdge("f","e",1)
G.addEdge("f","g",1)
G.addEdge("g","f",1)



prim(G.getVertex("a"),G)
'''
for v in G:
    print ("( %s , %d)" % (v.getId(),v.getDistance()))
'''