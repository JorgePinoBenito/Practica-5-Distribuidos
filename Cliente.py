import Pyro4 #importing Pyro4 library for RMI

Cliente = Pyro4.Proxy("PYRONAME:RMI.calculator") #creating a proxy for the client to connect to the server

eleccion = 0
numero1, numero2, numero3, resultado = 0.0, 0.0, 0.0, 0.0
menu = "\n\n------------------\n\n[-1] => Salir\n[0] => Sumar\n[1] => Restar\n[2] => Multiplicar\n[3] => Dividir\n[4] => Raiz\nElige: "
while eleccion != -1:
    print(menu)
    eleccion = input()
    
    try:
        eleccion = int(eleccion)
    except ValueError:
        eleccion = -1

    if eleccion != -1:
        match eleccion: #match expression to select the operation to be performed, emulates a switch statement in other languages. 
            case 0:
                print("Ingresa el número 1: ")
                try:
                    numero1 = float(input())
                except ValueError:
                    numero1 = 0.0

                print("Ingresa el número 2: ")
                try:
                    numero2 = float(input())
                except ValueError:
                    numero2 = 0.0

                print("Ingresa el número 3: ")
                try:
                    numero3 = float(input())
                except ValueError:
                    numero3 = 0.0

                resultado = Cliente.add(numero1, numero2, numero3)
                print("Resultado => " + str(resultado))
            case 1:
                print("Ingresa el número 1: ")
                try:
                    numero1 = float(input())
                except ValueError:
                    numero1 = 0.0

                print("Ingresa el número 2: ")
                try:
                    numero2 = float(input())
                except ValueError:
                    numero2 = 0.0

                resultado = Cliente.subtract(numero1, numero2)
                print("Resultado => " + str(resultado))
            case 2:
                print("Ingresa el número 1: ")
                try:
                    numero1 = float(input())
                except ValueError:
                    numero1 = 0.0

                print("Ingresa el número 2: ")
                try:
                    numero2 = float(input())
                except ValueError:
                    numero2 = 0.0

                resultado = Cliente.multiply(numero1, numero2)
                print("Resultado => " + str(resultado))
            case 3:
                print("Ingresa el número 1: ")
                try:
                    numero1 = float(input())
                except ValueError:
                    numero1 = 0.0

                print("Ingresa el número 2: ")
                try:
                    numero2 = float(input())
                except ValueError:
                    numero2 = 0.0

                resultado = Cliente.division(numero1, numero2)
                print("Resultado => " + str(resultado))
            case 4:
                print("Ingresa el número 1: ")
                try:
                    numero1 = float(input())
                except ValueError:
                    numero1 = 0.0

                resultado = Cliente.sqrt(numero1)
                print("Resultado => " + str(resultado))
            case _: #default case to handle invalid input
                print ("Opción no válida")

        print("Presiona ENTER para continuar")
        input()

