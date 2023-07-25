import getpass
import helpers 


userIdAttempts = 0

userId = ""
userName = ""
userPin = 0 
userDeposit = 0

arrayTipoCambio = helpers.tipoDeCambio()

minMoneyDolar = float(arrayTipoCambio[0]) #El primer dato del archivo de Conf Avanzada es el monto mínimo de deposito requerido en dolares
minMoneyColon = float(arrayTipoCambio[1]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a colones
minMoneyBitcoin = float(arrayTipoCambio[2]) * minMoneyDolar #El dato del archivo Conf Avanza es el valor de 1 dolar a bitcoins


def validateUserIdAttempts():
    totalUserIdValidAttempts = 3
    global userIdAttempts
    userIdAttempts += 1

    if (userIdAttempts == totalUserIdValidAttempts):
        print(
            f"\nHa excedido el máximo de {totalUserIdValidAttempts} intentos para ingresar un ID válido, volviendo al menú principal...")

        # importante importar aquí y no al inicio para evitar una importación circular entre ambos módulos
        helpers.returnToMainMenu()
    else:
        attemptsLeft = 3 - userIdAttempts
        print("\n>>> ID de usuario inválido, mínimo cinco caracteres. Le quedan "+str(attemptsLeft)+" intentos.") 
        addRegistration()


# def isUserExists(userId):
    # Esta función booleana valida si un usuario existe o no


def isValidUserId(userId):
    minUserIdLenght = 5
    return len(userId) >= minUserIdLenght


def validateUserId(userId):
    if isValidUserId(userId):
        # if isUserExists(userId):
        #  print("\nEste userId ya es ocupado por otro usuario, intente nuevamente...")
        #  return validateUserIdAttempts()
        return userId
    validateUserIdAttempts()


def getUserId():
    userId = input("Ingrese su ID (debe contener al menos cinco caractéres):\n> ")
    return validateUserId(userId)


# >>> Escogencia de PIN
# Solicitar al usuario que cree su PIN
def createPIN():
    while True:
        try:
            userPin = int(getpass.getpass("Digite su PIN (debe contener al menos 6 dígitos):\n> "))
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
            confirmPin = int(getpass.getpass("Digite nuevamente su PIN para confirmar:\n> "))
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
