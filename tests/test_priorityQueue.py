import sys
import unittest

sys.path.append("../")

from pythonds.graphs import PriorityQueue

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = PriorityQueue()
        self.theHeap.add((2,'x'))
        self.theHeap.add((3,'y'))
        self.theHeap.add((5,'z'))
        self.theHeap.add((6,'a'))
        self.theHeap.add((4,'d'))


    def testSize(self):
        assert self.theHeap.currentSize == 5

    def testInsert(self):
        self.theHeap.add((1,'t'))
        assert self.theHeap.heapArray[1] == (1,'t')

    def testContains(self):
        assert 'x' in self.theHeap

    def testDelmin(self):
        assert self.theHeap.delMin() == 'x'
        assert self.theHeap.delMin() == 'y'
    
    def testDecKey(self):
        self.theHeap.decreaseKey('d',1)
        assert self.theHeap.delMin() == 'd'
        
if __name__ == '__main__':
    unittest.main()