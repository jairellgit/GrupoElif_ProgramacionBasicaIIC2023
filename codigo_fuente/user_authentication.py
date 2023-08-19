import helpers
import getpass
import os

#Cuando se valide que existe el usuario, aqui se van a traer los valores del usuario (id, pin, nombre del usuario y dinero depositado). Para guardarlos en una lista
userIdTxt =  "jai123" #Dato temporal
userNameTxt = "Jairell" #Dato temporal
userMoneyTxt = 10000 #Dato temporal
userPinTxt = 123456 #Dato de prueba


def printMenu():

    print("\nMenú Opciones:")
    print("1) Retirar Dinero")
    print("2) Depositar Dinero")
    print("3) Ver saldo actual")
    print("4) Juegos en linea")
    print("5) Eliminar usuario")
    print("6) Salir")


def login():
    userIdAttempts = 0
    userPinAttempts = 0
    totalValidAttempts = 3

    #userIdTxt es la futura variable que va a contener el dato que venga de la base de datos (txt)
    while (userIdAttempts != 3):
        #En un futuro, esta variable se tiene enviar a la base de datos (txt), para validar que exista este usuario
        userId = input("Ingrese su ID (Usar: jai123):\n> ")

        if (userId == userIdTxt):

            while (userPinAttempts != 3):
                userPin = int(getpass.getpass("Digite su PIN (Usar: 123456):\n> "))
                #userPinTxt es la futura variable que va a contener el dato que venga de la base de datos (txt)
                if(userPin == userPinTxt):
                    menuCasino()
                    return userId, userPin, userNameTxt, userMoneyTxt
                else:
                    userPinAttempts += 1

                    if (userPinAttempts == totalValidAttempts):
                        print(f"\nHa excedido el máximo de {totalValidAttempts} intentos para iniciar sesión, volviendo al menú principal...")
                        helpers.returnToMainMenu()
                    else:
                        attemptsLeft = 3 - userPinAttempts
                        print(">>> El dato ingresado no es válido. Le quedan "+str(attemptsLeft)+" intentos.") 

        else:
            userIdAttempts += 1

            if (userIdAttempts == totalValidAttempts):
                print(f"\nHa excedido el máximo de {totalValidAttempts} intentos para iniciar sesión, volviendo al menú principal...")
                helpers.returnToMainMenu()
            else:
                attemptsLeft = 3 - userIdAttempts
                print(">>> El dato ingresado no es válido. Le quedan "+str(attemptsLeft)+" intentos.")
                

def menuCasino():
    print("\n♦♦♦ Hola "+userNameTxt+", ¡bienvenido/a al Dreamworld Casino! ♦♦♦")
    
    while True:

        printMenu()
        option = int(input("Digite la opcion que desee realizar:\n>"))

        if(option == 1):
            print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
        elif(option == 2):
            print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
        elif(option == 3):
            print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
        elif(option == 4):
            print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
        elif(option == 5):
            print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
        elif(option == 6):
            print("\n>>> Saliendo al menú principal...\n")
            helpers.returnToMainMenu()
        else:
            print("\n>>> Opción no válida. Inténtelo nuevamente\n")


def isUserExists(userId):
    return os.path.exists(f"users/{userId}")
