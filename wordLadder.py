
from pythonds.graphs import Graph
from bfs import bfs
d={}
g=Graph()
def buildGraph(list):
    for word in list:
        for i in range(len(word)):
            bucket=word[:i]+"_"+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else: d[bucket]=[word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if (word1!=word2):
                    g.addEdge(word1,word2)


'''
buildGraph(["hit","hot","dot","dog","lot","log","cog"])
for v in g:
   for w in v.getConnections():
       print("( %s , %s )" % (v.getId(), w.getId()))

bfs(g,g.getVertex("hit"),"cog")
'''

buildGraph(["fool","foul","foil","fail","fall","cool","pool",
"poll","pall","pole","pope","pale","sale","sage","page"])

bfs(g,g.getVertex("fool"),"sage")