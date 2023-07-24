import getpass
import os
import helpers

# Variables de ámbito global
userInfo = []
userIdAttempts = 0
userId = ""
userName = ""
userPin = 0 
userDeposit = 0

# >>> Escogencia de nombre de usuario
# Solicitar al usuario que cree su nombre de usuario


def getUsername():
    username = input("Ingrese su nombre de usuario: \n> ")
    return username

# >>> Escogencia de ID
# Solicitar al usuario que cree su ID


def validateUserIdAttempts():
    totalUserIdValidAttempts = 3
    userIdAttempts += 1

    if (userIdAttempts == totalUserIdValidAttempts):
        print(
            f"\nHa excedido el máximo de {totalUserIdValidAttempts} intentos para ingresar un ID válido, volviendo al menú principal...")

        helpers.returnToMainMenu()
    else:
        startUserRegistration()


def isUserExists(userId):
    return os.path.exists(f"users/{userId}")


def isValidUserId(userId):
    minUserIdLenght = 5
    return len(userId) >= minUserIdLenght


def validateUserId(userId):
    if isValidUserId(userId):
        if isUserExists(userId):
            print("\nEste userId ya es ocupado por otro usuario, intente nuevamente...")
            return validateUserIdAttempts()
        return userId

    print("\n>>> ID de usuario inválido, mínimo cinco caracteres...")
    validateUserIdAttempts()


def getUserId():
    userId = input(
        "Ingrese su ID (debe contener al menos cinco caractéres):\n> ")
    return validateUserId(userId)


# >>> Escogencia de PIN
# Solicitar al usuario que cree su PIN
def createPIN():
    while True:
        try:
            userPin = int(getpass.getpass(
                "Digite su PIN (debe contener al menos 6 dígitos):\n> "))
            if len(str(userPin)) >= 6:
                return str(userPin)
            else:
                print(
                    ">>> El PIN debe contener al menos 6 dígitos. Inténtelo nuevamente.")
        except ValueError:
            print(">>> Ingrese solo números.")


# Autenticar el PIN (confirmación)
def authenticatePin(userPin):
    while True:
        try:
            confirmPin = int(getpass.getpass(
                "Digite nuevamente su PIN para confirmar:\n> "))
            if userPin == str(confirmPin):
                print(">>> PIN creado con éxito.")
                return userPin
            else:
                print(">>> El PIN no coincide. Inténtelo nuevamente.")
        except ValueError:
            print(">>> Ingrese solo números.")


# Crear y autenticar el PIN
def getUserPin():
    userPin = createPIN()
    authenticatePin(userPin)
    return userPin


# >>> Depositar el dinero

# Monto temporal - Se configurará correctamente cuando estén los archivos de configuración avanzada
def getMinDeposit():
    return 10000


def getDeposit():
    global minMoney
    minMoney = getMinDeposit()
    depositAttempts = 0
    depositMoney = 0
    while (depositAttempts != 3) and (depositMoney < minMoney):
        try:
            depositMoney = float(
                input(f"Ingrese el monto a depositar para finalizar (mínimo ${minMoney}): \n> "))
            if (depositMoney >= minMoney):
                print("Deposito realizado con éxito. ¡Registro de usuario completado!")
                return depositMoney
            else:
                totalDepositValidAttempts = 3
                depositAttempts += 1

                if (depositAttempts == totalDepositValidAttempts):
                    print(
                        f"\nHa excedido el máximo de {totalDepositValidAttempts} intentos para realizar el depósito, volviendo al menú principal...")
                    helpers.returnToMainMenu()
                else:
                    attemptsLeft = 3 - depositAttempts
                    print(">>> El monto ingresado no es válido, debe ser mínimo $" +
                          str(minMoney)+". Le quedan "+str(attemptsLeft)+" intentos.")
        except ValueError:
            print(">>> Ingrese solo números.")

# >>> Guardado de información del usuario


def setCredentials():
    global userInfo

    userId = userInfo[0]
    userPin = userInfo[2]
    credentialsPath = "usuarios_pines.txt"

    appendMode = 'a'
    with open(credentialsPath, appendMode) as credentialsFile:
        credentialsFile.write(f"{userId}\n{userPin}\n")


def setDepositMoney():
    global userInfo

    userId = userInfo[0]
    userDepositMoney = userInfo[3]
    userPath = f"users/{userId}"

    os.makedirs(userPath)
    userPath += '/saldos.txt'

    # 'with' utilizado para cerrar archivos después de su uso.
    overwriteMode = 'w'
    with open(userPath, overwriteMode) as moneyFile:
        moneyFile.write(str(userDepositMoney))


def addRegistration():
    setDepositMoney()
    setCredentials()


# >>> Métodos principales del módulo


def getUserInfo():
    userId = getUserId()  # Punto 1
    userName = getUsername()  # Punto 2
    userPin = getUserPin()  # Punto 3

    userInfo = [userId, userName, userPin]
    return userInfo


def startUserRegistration():
    global userInfo

    print("\n♦ Registro de nuevo usuario")

    userInfo = getUserInfo()  # Engloba puntos 1, 2 y 3
    userInfo.append(getDeposit())  # Punto 4
    addRegistration()  # Punto 5
    helpers.returnToMainMenu()  # Punto 6