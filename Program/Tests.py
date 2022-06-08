import unittest
from serieFibonacci import Serie

class TestStringMethods(unittest.TestCase):

    def test_rango10(self):
        serie = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
        serie2 = Serie.getSerie(self,10)

        self.assertEqual(serie,serie2)
    
    def test_menores0(self):
        serie = Serie.getSerie(self,0)
        self.assertEqual(serie[0], 0)

    def test_caracteres(self):
        with  self.assertRaises(Exception):
            Serie.getSerie(self,"")

    def test_vacio(self):
         with  self.assertRaises(Exception):
            Serie.getSerie(self,None)

if __name__ == '__main__':
    unittest.main()