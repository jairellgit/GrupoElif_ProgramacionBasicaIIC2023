import helpers
import getpass
import user_registration

global userNameTxt
userNameTxt = ""


def login():
    userIdAttempts = 0
    userPinAttempts = 0
    totalValidAttempts = 3

    #Cuando se valide que existe el usuario, aqui se van a traer los valores del usuario (id, pin, nombre del usuario y dinero depositado). Para guardarlos en una lista
    userIdTxt =  "jai" #Dato temporal
    userNameTxt = "Jairell" #Dato temporal
    userMoneyTxt = 10000 #Dato temporal
    userPinTxt = 123456 #Dato de prueba

    #userIdTxt es la futura variable que va a contener el dato que venga de la base de datos (txt)
    while (userIdAttempts != 3):
        #En un futuro, esta variable se tiene enviar a la base de datos (txt), para validar que exista este usuario
        userId = input("Ingrese su ID:\n> ")

        if (userId == userIdTxt):

            while (userPinAttempts != 3):
                userPin = int(getpass.getpass("Digite su PIN:\n> "))
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
    print("\n♦♦♦ Hola "+userNameTxt+", bienvenido/a al Dreamworld Casino, ingrese la opcion que desee realizar ♦♦♦")
    
    while True:

        print("1) Retirar Dinero")
        print("2) Depositar Dinero")
        print("3) Ver saldo actual")
        print("4) Juegos en linea")
        print("5) Eliminar usuario")
        print("6) Salir")

        option = int(input("\n>"))

        if(option == 1):
            print()
        elif(option == 2):
            print()
        elif(option == 3):
            print()
        elif(option == 4):
            print()
        elif(option == 5):
            print()
        elif(option == 6):
            print()  
        else:
            print("Opción no válida. Inténtelo nuevamente")


#def userExists():
    #En este metodo se valida que en el archivo exista al menos un usuario