#genera los test de servidor y de cliente de este programa

import unittest
import Pyro4

Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")

class Test_Cliente_Servidor(unittest.TestCase):
    def test_1(self):
        #Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")
        resultado = Cliente.add(1, 2, 3)
        self.assertEqual(resultado, 5)

    def test_2(self):
        #Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")
        resultado = Cliente.subtract(1, 2)
        self.assertEqual(resultado, -1)

    def test_3(self):
        #Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")
        resultado = Cliente.multiply(1, 2)
        self.assertEqual(resultado, 2)

    def test_4(self):
        #Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")
        resultado = Cliente.division(1, 2)
        self.assertEqual(resultado, 0.5)
    
    def test_5(self):
        #Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator")
        resultado = Cliente.sqrt(4)
        self.assertEqual(resultado, 2.0)
        
if __name__ == '__main__': 
    unittest.main()


