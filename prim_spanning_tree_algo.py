from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(G, start):
    pq = PriorityQueue()

    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getDistance() \
            + currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)


def build_graph():
    graph = Graph()
    graph.addEdge('A', 'B', 2)
    graph.addEdge('B', 'A', 2)
    graph.addEdge('A', 'C', 3)
    graph.addEdge('C', 'A', 3)
    graph.addEdge('B', 'C', 1)
    graph.addEdge('C', 'B', 1)
    graph.addEdge('B', 'D', 1)
    graph.addEdge('D', 'B', 1)
    graph.addEdge('B', 'E', 4)
    graph.addEdge('E', 'B', 4)
    graph.addEdge('D', 'E', 1)
    graph.addEdge('E', 'D', 1)
    graph.addEdge('E', 'F', 1)
    graph.addEdge('F', 'E', 1)
    graph.addEdge('C', 'F', 5)
    graph.addEdge('F', 'C', 5)
    graph.addEdge('F', 'G', 1)
    graph.addEdge('G', 'F', 1)
 
    return graph

graph = build_graph()

prim(graph, graph.getVertex('A'))

temp_list = [ve for ve in graph]
temp_list.sort(key=lambda x:x.getDistance())

for ve in temp_list:
    print(ve.getId(), ':', ve.getDistance())
