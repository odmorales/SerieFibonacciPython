import unittest
from serieFibonacci import Serie

class TestStringMethods(unittest.TestCase):

    def test_rango10(self):
        serie = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
        serie2 = Serie.getSerie(self,10)

        self.assertEqual(serie,serie2)
    

if __name__ == '__main__':
    unittest.main()