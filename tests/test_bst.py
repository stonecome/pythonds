import sys
import unittest

sys.path.append("../")

from pythonds.trees import BinarySearchTree

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        
    def testgetput(self):
        print('testgetput')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        print(self.bst.get(50))
        assert self.bst.get(50) == 'a'
        assert self.bst.get(45) == 'f'
        assert self.bst.get(85) == 'd'
        assert self.bst.get(10) == 'b'
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 10
        assert self.bst.root.rightChild.key == 70
        
    def testputoper(self):
        print('testputoper')
        self.bst[25] = 'g'
        assert self.bst[25] == 'g'
        
    def testFindSucc(self):
        print('testing findSucc')
        x = BinarySearchTree()
        x.put(10,'a')
        x.put(15,'b')
        x.put(6,'c')
        x.put(2,'d')
        x.put(8,'e')
        x.put(9,'f')
        assert x.root.leftChild.leftChild.findSuccessor().key == 6
        assert x.root.leftChild.rightChild.findSuccessor().key == 9
        assert x.root.leftChild.rightChild.rightChild.findSuccessor().key == 10
        
    def testSize(self):
        print('testing testSize')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        assert self.bst.length() == 7
        
    def testDelete(self):
        print('testing delete')
        self.bst.put(50,'a')
        self.bst.put(10,'b')
        self.bst.put(70,'c')
        self.bst.put(30,'d')
        self.bst.put(85,'d')
        self.bst.put(15,'e')
        self.bst.put(45,'f')
        self.bst.put(5,'g')
        print('initial inorder')
        self.bst.inorder()
        assert (10 in self.bst) == True        
        self.bst.delete(10)
        print('delete 10 inorder')
        self.bst.inorder()        
        assert (10 in self.bst) == False
        assert self.bst.root.leftChild.key == 15
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        assert self.bst.get(30) == 'd'
        self.bst.delete(15)
        print('delete 15 inorder')
        self.bst.inorder()
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.leftChild.rightChild.key == 45
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        self.bst.delete(70)
        print('delete 70 inorder')        
        self.bst.inorder()        
        assert (85 in self.bst) == True
        assert self.bst.get(30) == 'd'
        print('root key = ', self.bst.root.key)
        print('left = ',self.bst.root.leftChild.key)
        print('left left = ',self.bst.root.leftChild.leftChild.key)
        print('left right = ',self.bst.root.leftChild.rightChild.key)        
        print('right = ',self.bst.root.rightChild.key)
        self.bst.delete(50)
        assert self.bst.root.key == 85
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild == None
        assert self.bst.root.leftChild.leftChild.key == 5
        assert self.bst.root.leftChild.rightChild.key == 45
        assert self.bst.root.leftChild.leftChild.parent == self.bst.root.leftChild
        assert self.bst.root.leftChild.rightChild.parent == self.bst.root.leftChild
        print('new root key = ', self.bst.root.key)
        self.bst.inorder()
        self.bst.delete(45)
        assert self.bst.root.leftChild.key == 30
        self.bst.delete(85)
        assert self.bst.root.key == 30
        print('xxxx ',self.bst.root.leftChild.parent.key, self.bst.root.key)
        assert self.bst.root.leftChild.parent == self.bst.root
        self.bst.delete(30)
        assert self.bst.root.key == 5
        self.bst.inorder()
        print("final root = " + str(self.bst.root.key))
        assert self.bst.root.key == 5
        self.bst.delete(5)
        assert self.bst.root == None

    def testDel2(self):
        self.bst.put(21,'a')
        self.bst.put(10,'b')
        self.bst.put(24,'c')
        self.bst.put(11,'d')
        self.bst.put(22,'d')
        self.bst.delete(10)
        assert self.bst.root.leftChild.key == 11
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.key == 24
        self.bst.delete(24)
        assert self.bst.root.rightChild.key == 22
        assert self.bst.root.rightChild.parent == self.bst.root
        self.bst.delete(22)
        self.bst.delete(21)
        print("del2 root = ",self.bst.root.key)
        assert self.bst.root.key == 11
        assert self.bst.root.leftChild == None
        assert self.bst.root.rightChild == None        

    def testLarge(self):
        import random
        print('testing a large random tree')
        i = 0
        randList = []
        while i < 10000:
            nrand = random.randrange(1,10000000)
            if nrand not in randList:
                randList.append(nrand)
                i += 1
        print(randList)
        for n in randList:
            self.bst.put(n,n)
        sortList = randList[:]
        sortList.sort()
        random.shuffle(randList)
        for n in randList:
            minNode = self.bst.root.findMin()
            if minNode:
                assert minNode.key == sortList[0]
            rootPos = sortList.index(self.bst.root.key)
            succ = self.bst.root.findSuccessor()
            if succ:
                assert succ.key == sortList[rootPos+1]
            else:
                assert self.bst.root.rightChild == None
            self.bst.delete(n)
            sortList.remove(n)
            
        assert self.bst.root == None

    def testIter(self):
        import random
        i = 0
        randList = []
        while i < 100:
            nrand = random.randrange(1,10000)
            if nrand not in randList:
                randList.append(nrand)
                i += 1
        for n in randList:
            self.bst.put(n,n)
        sortList = randList[:]
        sortList.sort()

        i = 0
        for j in self.bst:
            assert j == sortList[i]
            i += 1
# the following exercises all of the branches in deleting a node with one child
    def testCase1(self):
        self.bst.put(10,10)
        self.bst.put(7,7)
        self.bst.put(5,5)
        self.bst.put(1,1)
        self.bst.put(6,6)
        self.bst.delete(7)
        assert self.bst.root.leftChild.key == 5
        assert self.bst.root == self.bst.root.leftChild.parent
        assert self.bst.root.leftChild.leftChild.key == 1
        assert self.bst.root.leftChild.rightChild.key == 6

    def testCase2(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(15,15)
        self.bst.put(12,12)
        self.bst.put(11,11)
        self.bst.put(13,13)
        self.bst.delete(15)
        assert self.bst.root.rightChild.key == 12
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.rightChild.leftChild.key == 11
        assert self.bst.root.rightChild.rightChild.key == 13

    def testCase3(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(6,6)
        self.bst.put(8,8)
        self.bst.put(7,7)
        self.bst.put(9,9)
        self.bst.delete(6)
        assert self.bst.root.leftChild.key == 8
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.leftChild.leftChild.key == 7
        assert self.bst.root.leftChild.rightChild.key == 9

    def testCase4(self):
        self.bst = BinarySearchTree()
        self.bst.put(10,10)
        self.bst.put(15,15)
        self.bst.put(20,20)
        self.bst.put(17,17)
        self.bst.put(22,22)
        self.bst.delete(15)
        assert self.bst.root.rightChild.key == 20
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.rightChild.rightChild.key == 22
        assert self.bst.root.rightChild.leftChild.key == 17

    def testCase5(self):
        self.bst.put(10,10)
        self.bst.put(20,20)
        self.bst.put(17,17)
        self.bst.put(22,22)
        self.bst.delete(10)
        assert self.bst.root.key == 20
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.leftChild.key == 17
        assert self.bst.root.rightChild.key == 22

    def testCase6(self):
        self.bst.put(10,10)
        self.bst.put(5,5)
        self.bst.put(1,1)
        self.bst.put(7,7)
        self.bst.delete(10)
        assert self.bst.root.key == 5
        assert self.bst.root.leftChild.parent == self.bst.root
        assert self.bst.root.rightChild.parent == self.bst.root
        assert self.bst.root.leftChild.key == 1
        assert self.bst.root.rightChild.key == 7

    def testBadDelete(self):
        self.bst.put(10,10)
        with self.assertRaises(KeyError):
            self.bst.delete(5)
        self.bst.delete(10)
        with self.assertRaises(KeyError):
             self.bst.delete(5)

if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()

### Local Variables:
### End: