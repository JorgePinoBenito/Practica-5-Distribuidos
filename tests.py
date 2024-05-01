import unittest #importing unittest library for testing
import Pyro4 #importing Pyro4 library for RMI

Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator") #creating a proxy for the client to connect to the server

class Test_Cliente_Servidor(unittest.TestCase): #class for testing the client and server
    def test_1(self): #method for testing the addition operation
        resultado = Cliente.add(1, 2, 3) #testing the addition operation
        self.assertEqual(resultado, 6) #asserting the result of the addition operation

    def test_2(self): #method for testing the subtraction operation
        resultado = Cliente.subtract(1, 2)
        self.assertEqual(resultado, -1)

    def test_3(self): #method for testing the multiplication operation
        resultado = Cliente.multiply(1, 2)
        self.assertEqual(resultado, 2)

    def test_4(self): #method for testing the division operation
        resultado = Cliente.division(1, 2)
        self.assertEqual(resultado, 0.5)
     
    def test_5(self): #method for testing the square root operation
        resultado = Cliente.sqrt(4)
        self.assertEqual(resultado, 2.0)
        
if __name__ == '__main__': #main method to run the tests
    unittest.main()  


