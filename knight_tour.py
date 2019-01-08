'''
The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once. One such sequence is called a “tour.”
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

    def dfs_visit(self, startv):
        startv.setColor('gray')
        self.time += 1
        startv.setDiscovery(self.time)
        for nextv in startv.getConnections():
            if nextv.getColor() == 'white':
                nextv.setPred(startv)
                self.dfs_visit(nextv)

        startv.setColor('black')
        self.time += 1
        startv.setFinish(self.time)

def knight_graph(board_size):
    knight_graph = DFSGraph()
    for row in range(board_size):
        for col in range(board_size):
            nodeid = posToNodeId(row,col,board_size)
            new_positions = genLegalMoves(row,col, board_size)
            for e in new_positions:
                nid = posToNodeId(e[0], e[1], board_size)
                knight_graph.addEdge(nodeid, nid)
    return knight_graph

def posToNodeId(row, column, board_size):
    return row * board_size + column

def genLegalMoves(x, y, board_size):
    newMoves = []
    moveoffsets = [(-1,-2), (-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in moveoffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, board_size) and legalCoord(newY,board_size):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, board_size):
    if x >=0 and x < board_size:
        return True
    else:
        return False

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]
#  n, the current depth in the search tree; 
#  path, a list of vertices visited up to this point; 
# u, the vertex in the graph we wish to explore; 
# limit the number of nodes in the path. 
def knight_tour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        # Warnsdorff’s algorithm
        nbrlist = orderByAvail(u)
        # nbrlist = list(u.getConnections())
        i = 0
        done = False
        while i<len(nbrlist) and not done:
            if nbrlist[i].getColor() == 'white':
                # print(nbrlist[i].getId())
                done = knight_tour(n+1, path, nbrlist[i], limit)
            i = i + 1

        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

knight_graph = knight_graph(8)

#for v in knight_graph:
#    print(v.getId(),':', v.connectedTo)

u = knight_graph.getVertex(0)
path = []
knight_tour(0, path,u,63)

for i in path:
    print(i.getId(), end = ' ')
print('\n')

for i in path:
    i.setColor('white')

knight_graph.dfs_visit(knight_graph.getVertex(0))

for v in knight_graph:
    print(v.getId(),'-',v.getFinish(), end = '|')
