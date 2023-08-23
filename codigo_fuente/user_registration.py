import getpass
import helpers
import os

# >>> Variables
userInfo = []
userIdAttempts = 0

userId = ""
userName = ""
userPin = 0
userDeposit = 0

arrayTipoCambio = helpers.confAvanzada()

# >>> Escogencia de ID
# Solicitar al usuario que cree su ID


def validateUserIdAttempts():
    totalUserIdValidAttempts = 3
    global userIdAttempts
    userIdAttempts += 1

    if (userIdAttempts == totalUserIdValidAttempts):
        print(
            f"\nHa excedido el máximo de {totalUserIdValidAttempts} intentos para ingresar un ID válido, volviendo al menú principal...")

        helpers.returnToMainMenu()
    else:
        attemptsLeft = 3 - userIdAttempts
        print("\n>>> ID de usuario inválido, mínimo cinco caracteres. Le quedan " +
              str(attemptsLeft)+" intentos.")
        # addRegistration()
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
                    "\n>>> El PIN debe contener al menos 6 dígitos. Inténtelo nuevamente.\n")
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

# Menú opciones deposito
def printMenuMoneyType(id):
    print("\nDepósito:")
    print("1) Colones")
    print("2) Dólares")
    print("3) Bitcoin")


# Convertir el dinero
def convertMoney(depositMoney, moneyType):
    listaTipoDeCambio = helpers.confAvanzada()

    if moneyType == 1:  # Valor equivalente de 1 Dolar a Colones
        valorColon = float(listaTipoDeCambio[1])
        ConvDepositMoney = depositMoney / valorColon
    elif moneyType == 3:  # Valor equivalente de 1 Dolar a Bitcoins
        valorBitcoin = float(listaTipoDeCambio[2])
        ConvDepositMoney = depositMoney / valorBitcoin
    else:  # Dólares
        ConvDepositMoney = depositMoney

    return ConvDepositMoney


# Dinero minimo para cada tipo de moneda
def getMinMoney(moneyType):
    # El primer dato del archivo de Conf Avanzada es el monto mínimo de deposito requerido en dolares
    minMoneyDolar = float(arrayTipoCambio[0])
    # El dato del archivo Conf Avanza es el valor de 1 dolar a colones
    minMoneyColon = float(arrayTipoCambio[1]) * minMoneyDolar
    # El dato del archivo Conf Avanza es el valor de 1 dolar a bitcoins
    minMoneyBitcoin = float(arrayTipoCambio[2]) * minMoneyDolar

    dictionayMinMoneyValues = {
        1: minMoneyColon,
        2: minMoneyDolar,
        3: minMoneyBitcoin
    }
    return dictionayMinMoneyValues.get(moneyType, 0)


# Realizar deposito
def processDeposit(id, moneyType):
    minMoney = getMinMoney(moneyType)
    depositAttempts = 0

    while depositAttempts < 3:
        try:
            depositMoney = float(input(f"Ingrese el monto a depositar (mínimo {getMinMoney(moneyType)}): \n>"))
            if depositMoney >= minMoney:
                convertedMoney = convertMoney(depositMoney, moneyType)
                print(f"\n>>> Deposito realizado con éxito. ¡Registro de usuario completado!")
                return convertedMoney
            else:
                depositAttempts += 1
                attemptsLeft = 3 - depositAttempts
                print(f"\n>>> El monto ingresado no es válido, debe equivaler mínimo a {minMoney}. Le quedan {attemptsLeft} intentos.")
        except ValueError:
            print("\n>>> Ingrese solo números.")

    if (depositAttempts == 3):
        print(">>> Ha excedido el máximo de intentos para realizar el depósito, volviendo al menú principal...")
        helpers.returnToMainMenu()
    


# Función general para el deposito
def depositMoney(id):
    printMenuMoneyType(id)
    moneyType = int(input(
        "Digite el número de opción correspondiente al tipo de moneda que desea depositar: \n> "))

    return processDeposit(id, moneyType)


# >>> Guardado de información del usuario
def setCredentials():
    global userInfo

    userId = userInfo[0]
    userName = userInfo[1]
    userPin = userInfo[2]
    credentialsPath = "usuarios_pines.txt"

    appendMode = 'a'
    with open(credentialsPath, appendMode) as credentialsFile:
        credentialsFile.write(f"{userId}\n{userName}\n{userPin}\n")


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
    userName = input("Ingrese su nombre: \n> ")  # Punto 2
    userPin = getUserPin()  # Punto 3

    userInfo = [userId, userName, userPin]
    return userInfo


def resetGlobalValues():
    global userIdAttempts
    totalUserIdValidAttempts = 3

    if userIdAttempts >= totalUserIdValidAttempts:
        userIdAttempts = 0


def startUserRegistration():
    global userInfo

    print("\n♦ Registro de nuevo usuario")

    resetGlobalValues()
    userInfo = getUserInfo()  # Engloba puntos 1, 2 y 3
    userInfo.append(depositMoney(userInfo[0]))  # Punto 4
    addRegistration()  # Punto 5
    helpers.returnToMainMenu()  # Punto 6
