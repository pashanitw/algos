from pythonds.graphs import Graph

def Dfs(currentVertex):
    currentVertex.setColor("gray")
    for vertex in currentVertex.getConnections():
        if vertex.getColor()=="white":
            Dfs(vertex)
    currentVertex.setColor("black")
    print currentVertex.getId()

g=Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(4,1)
g.addEdge(5,2)

Dfs(g.getVertex(0))

