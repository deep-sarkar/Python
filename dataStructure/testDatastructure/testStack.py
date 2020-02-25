import unittest
import os.path, sys 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from stack import *

my_stack = Stack()
my_stack.push("green")
my_stack.push("black")
my_stack.push("blue")
my_stack.push("red")
my_stack.push("white")

class testStack(unittest.TestCase):
    def testPeek(self):
        self.assertEqual(my_stack.peek(),"white")

    def testPop(self):
        self.assertEqual(my_stack.pop(),"white")
        self.assertNotEqual(my_stack.pop(),"white")
    
    def testSize(self):
        self.assertEqual(my_stack.size(),3)
    
    def testEmpty(self):
        self.assertFalse(my_stack.is_empty())


if __name__ == "__main__":
    unittest.main()