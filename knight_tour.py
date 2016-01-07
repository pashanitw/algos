import sys
sys.setrecursionlimit(1000000000)
from pythonds.graphs import Graph
g=Graph()

def getId(row,column,size):
    return row*size+column

def inDifferentRows(id1,id2,size):
    return not int(id1/size)==int(id2/size)
def getTupleFromId(id,size):
    return

def isTupleValid(nodeId,tuple,size):
    tup1=(int(nodeId/size),nodeId%size)
    newTuple=(tup1[0]+tuple[0],tup1[1]+tuple[1])
    return (newTuple[0] in range(size)) & (newTuple[1] in range(size))

def getPossibleNodeIds(size,nodeId):
    validIds=[]
    tuples=[(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(2,-1),(-2,1),(2,1)]
    for tup in tuples:
        connectionId=nodeId+getId(tup[0],tup[1],size)
        if isTupleValid(nodeId,tup,size):
            validIds.append(connectionId)
    if(nodeId==13):
        print validIds
    return validIds

def buildGraph(size):
    for i in range(size):
        for j in range(size):
            nodeId=getId(i,j,size)
            connections=getPossibleNodeIds(size,nodeId)
            length=len(connections)
            for k in range(length):
                g.addEdge(nodeId,connections[k])
'''
def knightTour(start,n,limit,path):
    print start.getId()
    start.setColor('gray')

    done=False
    if(n<limit):
        connections=start.getConnections()
        for connection in connections:
            if (not done) & (connection.getColor()=="white"):
                done=knightTour(connection,n+1,limit,path)

    if(n==limit):
        done=True
    if(done):
        path.append(start.getId())
        print "Fucking Done"
        return done
    else:
        print "Fucking backtrack"
        start.setColor("white")

'''
def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    print u.getId()
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                print "backtrack at", u.getId()
                u.setColor('white')
        else:
            done = True
            print "yes done"
        return done



buildGraph(4)

path=[]
knightTour(1,path,g.getVertex(0),16)
print path,len(path)
print path
