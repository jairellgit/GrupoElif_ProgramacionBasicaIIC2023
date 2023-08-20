import getpass
import helpers 
import os

# Variables de ámbito global
userInfo = []
userIdAttempts = 0

userId = ""
userName = ""
userPin = 0 
userDeposit = 0

arrayTipoCambio = helpers.tipoDeCambio()

minMoneyDolar = float(arrayTipoCambio[0]) #El primer dato del archivo de Conf Avanzada es el monto mínimo de deposito requerido en dolares
minMoneyColon = float(arrayTipoCambio[1]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a colones
minMoneyBitcoin = float(arrayTipoCambio[2]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a bitcoins


# >>> Escogencia de nombre de usuario
# Solicitar al usuario que cree su nombre de usuario
def getUsername():
    username = input("Ingrese su nombre de usuario: \n> ")
    return username

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
        print("\n>>> ID de usuario inválido, mínimo cinco caracteres. Le quedan "+str(attemptsLeft)+" intentos.") 
        #addRegistration()
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
                print("\n>>> El PIN debe contener al menos 6 dígitos. Inténtelo nuevamente.\n")
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
def printMenuMoneyType():

    print("\nDepósito:")
    print("1) Colones")
    print("2) Dólares")
    print("3) Bitcoin")


# Contador de intentos
def attemptsDeposit(depositMoney, depositAttempts, type):
    minimo = 0
    if (type == 1):
        minimo = minMoneyColon
    elif (type == 2):
        minimo = minMoneyDolar
    elif (type == 3):
        minimo = minMoneyBitcoin
        
    if(depositMoney >= minMoneyDolar):
        print("\n>>> Deposito realizado con éxito. ¡Registro de usuario completado!")
        flagDeposit = True
        return depositMoney, 3, flagDeposit
    else: 
        totalDepositValidAttempts = 3
        depositAttempts += 1

        if (depositAttempts == totalDepositValidAttempts):
            print(f"\nHa excedido el máximo de {totalDepositValidAttempts} intentos para realizar el depósito, volviendo al menú principal...")
            helpers.returnToMainMenu()
        else:
            attemptsLeft = 3 - depositAttempts
            if (type == 1): #Colones
                print("\n>>> El monto ingresado no es válido, debe equivaler mínimo a ₡"+str(minMoneyColon)+". Le quedan "+str(attemptsLeft)+" intentos.") 
            elif (type == 2): #Dolares
                print("\n>>> El monto ingresado no es válido, debe equivaler mínimo a $"+str(minMoneyDolar)+". Le quedan "+str(attemptsLeft)+" intentos.") 
            elif (type == 3): #Bitcoin
                print("\n>>> El monto ingresado no es válido, debe equivaler mínimo a ₿"+str(minMoneyBitcoin)+". Le quedan "+str(attemptsLeft)+" intentos.") 

        return depositMoney, depositAttempts, False


# Convertir el dinero
def convertMoney(depositMoney, moneyType):
    listaTipoDeCambio = helpers.tipoDeCambio()

    if moneyType == 1: #Valor equivalente de 1 Dolar a Colones
        valorColon = float(listaTipoDeCambio[1])        
        ConvDepositMoney = depositMoney / valorColon
    elif moneyType == 3: #Valor equivalente de 1 Dolar a Bitcoins
        valorBitcoin = float(listaTipoDeCambio[2])
        ConvDepositMoney = depositMoney / valorBitcoin
    else: #Dólares
        ConvDepositMoney = depositMoney

    return ConvDepositMoney


# Función general para el deposito
def getDeposit(depositMoney, depositAttempts): 
    flagDeposit = False

    while (depositAttempts != 3):
        try:
            printMenuMoneyType()
            moneyType = int(input(f"Digite el número de opción correspondiente al tipo de moneda que desea depositar: \n> "))

            #Se le indica el monto mínimo según la opción elegida 
            if moneyType == 1: #Colones
                depositMoney = float(input(f"Ingrese el monto a depositar para finalizar (mínimo ₡{minMoneyColon}): \n> "))
                depositMoneyConverted = convertMoney(depositMoney, moneyType)
                print("Dinero a doláres: "+ str(depositMoneyConverted))
                depositMoney, depositAttempts, flagDeposit = attemptsDeposit(depositMoneyConverted, depositAttempts, 1)

            elif moneyType == 2: #Dólares
                depositMoney = float(input(f"Ingrese el monto a depositar para finalizar (mínimo ${minMoneyDolar}): \n> "))
                depositMoneyConverted = convertMoney(depositMoney, moneyType)
                print("Dinero a doláres: "+ str(depositMoneyConverted))
                depositMoney, depositAttempts, flagDeposit = attemptsDeposit(depositMoneyConverted, depositAttempts, 2)

            elif moneyType == 3: #Bitcoin
                depositMoney = float(input(f"Ingrese el monto a depositar para finalizar (mínimo ₿{minMoneyBitcoin}): \n> "))
                depositMoneyConverted = convertMoney(depositMoney, moneyType)
                print("Dinero a doláres: "+ str(depositMoneyConverted))
                depositMoney, depositAttempts, flagDeposit = attemptsDeposit(depositMoneyConverted, depositAttempts, 3)

            else:
                print("\n>>> Opción no válida. Inténtelo nuevamente")
        except ValueError:
            print("\n>>> Ingrese solo números.")
    return depositMoney, flagDeposit

  
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
    userName = getUsername()  # Punto 2
    userPin = getUserPin()  # Punto 3

    userInfo = [userId, userName, userPin]
    return userInfo


def startUserRegistration():
    depositMoney = 0
    depositAttempts = 0
    global userInfo

    print("\n♦ Registro de nuevo usuario")

    userInfo = getUserInfo()  # Engloba puntos 1, 2 y 3
    userInfo.append(getDeposit(depositMoney, depositAttempts)) # Punto 4
    addRegistration()  # Punto 5
    helpers.returnToMainMenu()  # Punto 6
