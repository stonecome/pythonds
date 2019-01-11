import sys
import unittest

sys.path.append("../")

from pythonds.trees import AVLTree

class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = AVLTree()

    def testAuto1(self):
        self.bst.put(30,'a')
        self.bst.put(50,'b')
        self.bst.put(40,'c')
        assert self.bst.root.key == 40

    def testAuto2(self):
        self.bst.put(50,'a')
        self.bst.put(30,'b')
        self.bst.put(40,'c')
        assert self.bst.root.key == 40

    def testAuto3(self):
        self.bst.put(50,'a')
        self.bst.put(30,'b')
        self.bst.put(70,'c')
        self.bst.put(80,'c')
        self.bst.put(60,'d')
        self.bst.put(90,'e')
        assert self.bst.root.key == 70

    def testAuto3(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(45,'d')
        self.bst.put(60,'e')
        self.bst.put(43,'f')
        assert self.bst.root.key == 45
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1

    def testAuto4(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(10,'d')
        self.bst.put(35,'e')
        self.bst.put(37,'f')
        assert self.bst.root.key == 35
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild.key == 40
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.rightChild.balanceFactor == 0


if __name__ == '__main__':
    import platform
    print(platform.python_version())
    unittest.main()

# Local Variables:
# py-which-shell: "python3"
# End: