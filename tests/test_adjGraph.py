import sys
import unittest

sys.path.append("../")

from pythonds.graphs import Graph

class adjGraphTests(unittest.TestCase):
    def setUp(self):
        self.tGraph = Graph()
        
    def testMakeGraph(self):
        with open("test.dat") as gFile:
            for line in gFile:
                fVertex, tVertex = line.split('|')
                fVertex = int(fVertex)
                tVertex = int(tVertex)
                self.tGraph.addEdge(fVertex,tVertex)
        
        for i in self.tGraph:
            adj = i.getConnections()
            for k in adj:
                print(i.getId(), k.getId())

        
if __name__ == '__main__':
    unittest.main()