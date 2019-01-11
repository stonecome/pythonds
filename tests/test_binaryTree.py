import sys
import unittest

sys.path.append("../")

from pythonds.trees.binaryTree import *

if __name__ == '__main__':
    t = BinaryTree(7)
    t.insertLeft(3)
    t.insertRight(9)
    inorder(t)
    x = BinaryTree('*')
    x.insertLeft('+')
    l = x.getLeftChild()
    l.insertLeft(4)
    l.insertRight(5)
    x.insertRight(7)
    print(printexp(x))
    print(postordereval(x))
    print(height(x))