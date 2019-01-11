import sys
import unittest

sys.path.append("../")

from pythonds.trees import BinHeap

class FooThing:
    def __init__(self,x,y):
        self.key = x
        self.val = y
        

    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = BinHeap()
        self.theHeap.insert(FooThing(5,'a'))                               
        self.theHeap.insert(FooThing(9,'d'))                  
        self.theHeap.insert(FooThing(1,'x'))
        self.theHeap.insert(FooThing(2,'y'))
        self.theHeap.insert(FooThing(3,'z'))

    def testInsert(self):
        assert self.theHeap.currentSize == 5

    def testDelmin(self):
        assert self.theHeap.delMin().val == 'x'
        assert self.theHeap.delMin().val  == 'y'
        assert self.theHeap.delMin().val  == 'z'
        assert self.theHeap.delMin().val  == 'a'

    def testMixed(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(5)
        assert myHeap.delMin() == 1
        myHeap.insert(2)
        myHeap.insert(7)
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 5

    def testDupes(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(8)
        myHeap.insert(1)
        assert myHeap.currentSize == 4
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 8

    def testBuildHeap(self):
        myHeap = BinHeap()
        myHeap.buildHeap([9,5,6,2,3])
        f = myHeap.delMin()
        print("f = ", f)
        assert f == 2
        assert myHeap.delMin() == 3
        assert myHeap.delMin() == 5
        assert myHeap.delMin() == 6
        assert myHeap.delMin() == 9                        
        
if __name__ == '__main__':
    unittest.main()