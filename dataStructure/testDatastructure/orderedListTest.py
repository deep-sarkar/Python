import unittest
import os.path, sys 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
# import sys
# sys.path.insert(0,'/python/Python/dataStructure')
from utilOrderedList import *


o = OrderedList()
o.add(54)
o.add(12)
o.add(34)
o.add(25)
o.add(9)

class TestOrderedList(unittest.TestCase):
    def testSearch(self):
        self.assertEqual(o.search(10),False)
        self.assertEqual(o.search(12),True)

    def testIndex(self):
        self.assertEqual(o.index(12),1)
        self.assertEqual(o.index(100),-1)

    def testEmpty(self):
        self.assertFalse(o.empty())

    def testPop(self):
        self.assertNotEqual(o.pop(),22)
    
    def testPopIndex(self):
        self.assertEqual(o.pop_index(3),34)

    def testSize(self):
        self.assertEqual(o.size(),3)
    
if __name__ == '__main__':
    unittest.main()