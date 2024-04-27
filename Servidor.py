import Pyro4 #importing Pyro4 library for RMI
import math #importing math library for mathematical operations

@Pyro4.expose #exposing the class to the client

class Server(object): #class for the server to perform the operations, object is the parent class of the class Server 

    def add(self, a, b, c): #method for addition of three numbers a and b. Self is used to refer to the instance of the class
        return (a+b+c) #returning the result of addition

    def subtract(self, a, b): #method for subtraction of two numbers a and b. Self is used to refer to the instance of the class
        return (a-b) #returning the result of subtraction

    def multiply(self, a, b): #method for multiplication of two numbers a and b. Self is used to refer to the instance of the class
        return (a*b) #returning the result of multiplication

    def division(self, a, b): #method for division of two numbers a and b. Self is used to refer to the instance of the class
        if b == 0:
            return "Division by zero is not allowed"
        else:
            return (a/b) #returning the result of division

    def sqrt(self, a): #method for square root of a number a. Self is used to refer to the instance of the class
        return (math.sqrt(a)) #returning the result of square root

daemon = Pyro4.Daemon(host="localhost", port=8000) #creating a daemon for the server 
ns = Pyro4.locateNS() #locating the Name Server to register the server
url = daemon.register(Server) #registering the server with the daemon
ns.register("RMI.calculator", url) #registering the server with the Name Server

print("The Server is now active, please request your calculations or start file transfer")

daemon.requestLoop() #starting the request loop for the server to listen to the client requests