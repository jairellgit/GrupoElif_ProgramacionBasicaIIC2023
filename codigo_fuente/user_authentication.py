import helpers
import menu_casino
import getpass
import os
import slots



def printMenu():
    print("\nMenú Opciones:")
    print("1) Retirar Dinero")
    print("2) Depositar Dinero")
    print("3) Ver saldo actual")
    print("4) Juegos en linea")
    print("5) Eliminar usuario")
    print("6) Salir")


# Inicio de sesión
def login():
    userIdAttempts = 0 # Contador intentos para insertar id
    userPinAttempts = 0 # Contador intentos para insertar pin
    totalValidAttempts = 3 # Intentos disponibles

    while userIdAttempts < totalValidAttempts:
        userId = input("Ingrese su ID: ")

        if isUserExists(userId): # Va a validar que el usuario exista
            userPinTxt = getUserPin(userId)
            while userPinAttempts < totalValidAttempts:
                userPin = int(getpass.getpass("Digite su PIN: "))
                if userPin == userPinTxt:
                    id, pin, name = getUserInfo(userId)
                    menuCasino(id, pin, name)
                else:
                    userPinAttempts += 1
                    attemptsLeft = totalValidAttempts - userPinAttempts
                    print(f">>> El dato ingresado no es válido. Le quedan {attemptsLeft} intentos.")
            else:
                print(f"\n>>> Ha excedido el máximo de {totalValidAttempts} intentos para el PIN, volviendo al menú principal...")
                helpers.returnToMainMenu()
        else:
            userIdAttempts += 1
            attemptsLeft = totalValidAttempts - userIdAttempts
            print(f">>> El dato ingresado no es válido. Le quedan {attemptsLeft} intentos.")
    
    print(f"\n>>> Ha excedido el máximo de {totalValidAttempts} intentos para iniciar sesión, volviendo al menú principal...")


# Valida que el usuario exista
def isUserExists(userId):
    return os.path.exists(f"users/{userId}")


# Obtiene el PIN del usuario
def getUserPin(userId):
    with open("usuarios_pines.txt", "r") as file:
        lines = file.readlines()
        index = lines.index(userId + "\n")
        return int(lines[index + 2])


# Obtiene toda la informarción del usuario en base al ID 
def getUserInfo(userId):
    with open("usuarios_pines.txt", "r") as file:
        lines = file.readlines()
        index = lines.index(userId + "\n")

        id = lines[index].strip() # Obtener usuario (ID)
        name = lines[index + 1].strip() # Obtener nombre
        pin = int(lines[index + 2])  # Obtener PIN

        return id, pin, name


# >>> Menú Principal después de iniciar sesión
def menuCasino(id, pin, name):
    print("\n♦♦♦ Hola "+name+", ¡bienvenido/a al Dreamworld Casino! ♦♦♦")

    while True:

        printMenu()
        option = int(input("\nDigite la opcion que desee realizar:\n>"))

        if(option == 1):
            print("\n♦ Retirar Dinero")
            menu_casino.withdrawMoney(id)
        elif(option == 2):
            print("\n♦ Depositar Dinero")
            menu_casino.depositMoney(id)
        elif(option == 3):
            print("\n♦ Saldo Actual")
            balance = menu_casino.getMoney(id)
            print(f">>> Saldo actual: ${balance:.4f}")
        elif(option == 4):
            print("\nMenú Juegos:")
            print("1) Blackjack")
            print("2) Tragamonedas")
            gameOption = int(input("Digite el juego que desee:\n>"))
            if(gameOption == 1):
                print("\n>>> La opción seleccionada no se encuentra en funcionamiento aún.\n")
            elif(gameOption == 2):
                slots.start(id,pin,name)
            else:
                print("\n>>> Opción no válida. Inténtelo nuevamente\n")
        elif(option == 5):
            print("\n♦ Eliminar Usuario")
            menu_casino.deleteUser(id, pin, name)
        elif(option == 6):
            print("\n>>> Saliendo al menú principal...\n")
            helpers.returnToMainMenu()
        else:
            print("\n>>> Opción no válida. Inténtelo nuevamente\n")
