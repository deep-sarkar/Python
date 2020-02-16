import unittest
from vendinMachine import *

class TestVendingMachine(unittest.TestCase):
    def test_vending_machine(self):
        vn = VendingMachine()
        self.assertEqual(vn.vending_machine(5372),11)
        self.assertEqual(vn.vending_machine(6384),14)
        self.assertEqual(vn.vending_machine(7482),15)

        with self.assertRaises(NameError):
            vn.vending_machine(gsj)


if __name__ == '__main__':
    unittest.main()