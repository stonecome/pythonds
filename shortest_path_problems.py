'''
The algorithm we are going to use to determine the shortest path is called “Dijkstra’s algorithm.” Dijkstra’s algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node to all other nodes in the graph. Again this is similar to the results of a breadth first search.

Dijkstra's Algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node to all other nodes in the graph.
'''

from pythonds.graphs import Graph, Vertex, PriorityQueue

def dijkstra(agraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in agraph])

    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
            + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)


def build_graph():
    graph = Graph()
    graph.addEdge('u', 'v', 2)
    graph.addEdge('v', 'u', 2)
    graph.addEdge('u', 'x', 1)
    graph.addEdge('x', 'u', 1)
    graph.addEdge('u', 'w', 5)
    graph.addEdge('w', 'u', 5)
    graph.addEdge('v', 'x', 2)
    graph.addEdge('x', 'v', 2)
    graph.addEdge('v', 'w', 3)
    graph.addEdge('w', 'v', 3)
    graph.addEdge('x', 'w', 3)
    graph.addEdge('w', 'x', 3)
    graph.addEdge('w', 'y', 1)
    graph.addEdge('y', 'w', 1)
    graph.addEdge('x', 'y', 1)
    graph.addEdge('y', 'x', 1)
    graph.addEdge('y', 'z', 1)
    graph.addEdge('z', 'y', 1)
    graph.addEdge('z', 'w', 5)
    graph.addEdge('w', 'z', 5)

    return graph

graph = build_graph()

dijkstra(graph, graph.getVertex('u'))

for ve in graph:
    print(ve.getId(), ':', ve.getDistance())