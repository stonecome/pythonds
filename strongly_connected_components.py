'''
let’s consider the difficult problem of stirring up a batch of pancakes. The recipe is really quite simple: 1 egg, 1 cup of pancake mix, 1 tablespoon oil, and 34 cup of milk. To make pancakes you must heat the griddle(a heavy flat plate), mix all the ingredients together and spoon the mix onto a hot griddle. When the pancakes start to bubble you turn them over and let them cook until they are golden brown on the bottom. Before you eat your pancakes you are going to want to heat up some syrup(a thick sweet liquid).
'''
from pythonds.graphs import Graph, Vertex

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for av in self:
            av.setColor('white')
            av.setPred(-1)
            for av in self:
                if av.getColor() == 'white':
                    self.dfs_visit(av)
                    print('')

    def dfs_visit(self, startv):
        startv.setColor('gray')
        print(startv.getId(), end=' ')
        self.time += 1
        startv.setDiscovery(self.time)
        for nextv in startv.getConnections():
            if nextv.getColor() == 'white':
                nextv.setPred(startv)
                self.dfs_visit(nextv)

        startv.setColor('black')
        self.time += 1
        startv.setFinish(self.time)

    def topological_sorting(self):
        for av in self:
            if av.getColor() == 'white':
                self.dfs_visit(av)

        return self.sort_by_finish_time()

    def sort_by_finish_time(self):
        resList = []
        for v in self:
            resList.append((v.getFinish(),v))

        resList.sort(key=lambda x:x[0], reverse = True)
        return [y[1] for y in resList]

def reverse_graph(graph):
    graph_t = DFSGraph()
    for v in graph:
        for nextv in v.getConnections():
            graph_t.addEdge(nextv.getId(), v.getId())

    return graph_t


def build_graph():
    graph = DFSGraph()
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.addEdge('B', 'E')
    graph.addEdge('C', 'F')
    graph.addEdge('E', 'A')
    graph.addEdge('E', 'D')
    graph.addEdge('D', 'B')
    graph.addEdge('D', 'G')
    graph.addEdge('G', 'E')
    graph.addEdge('F', 'H')
    graph.addEdge('H', 'I')
    graph.addEdge('I', 'F')

    return graph

graph = build_graph()

tmp_list = graph.topological_sorting()


for v in tmp_list:
    print(v.getId(),':',v.getFinish())

print('')

graph_t = reverse_graph(graph)
for v in graph_t:
    print(v.getId(), ':', [y.getId() for y in v.getConnections()])

for av in tmp_list:
    tmp_av = graph_t.getVertex(av.getId())
    if tmp_av.getColor() == 'white':
        # print('Visit: ', av.getId())
        graph_t.dfs_visit(tmp_av)
        print('')
