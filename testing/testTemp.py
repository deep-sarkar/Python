import unittest
from temperatureConversion import *

class TestTempConversion(unittest.TestCase):
#testing method fahrenheit to celsius conversion
    def test_fahrenheit_celsius(self):
        t = TempConversion()
        self.assertEqual(t.fahrenheit_celsius(100),38)
        self.assertEqual(t.fahrenheit_celsius(323),162)

        with self.assertRaises(NameError):
            t.fahrenheit_celsius(yrk)                      #passing string as an argument

#testing method celsius to fahrenheit conversion
    def test_celsius_fahrenheit(self) :
        t = TempConversion()
        self.assertEqual(t.celsius_fahrenheit(161),322)
        self.assertEqual(t.celsius_fahrenheit(37),99)

        with self.assertRaises(NameError):
            t.celsius_fahrenheit(psd)                    #passing string as an argument
#passing string as an argument


if __name__ == '__main__':
    unittest.main()