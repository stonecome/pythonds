from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def build_graph(word_file):
    d = {}
    g = Graph()

    wfile = open(word_file,'r')
    # Create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for word in d.keys():
        print(word,':', d[word])

    # Add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word2 != word1:
                    g.addEdge(word1, word2)

    return g


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size()>0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
        #print(currentVert)


word_graph = build_graph('words.dat')
start = word_graph.getVertex('fool')

bfs(word_graph, start)

#for v in word_graph:
#    print(v)

def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(word_graph.getVertex('sage'))
