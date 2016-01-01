'''
wfile = open("data.txt",'r')

for line in wfile:
    word=line[:-1].split()
    g.addEdge(word[0],word[1])
'''