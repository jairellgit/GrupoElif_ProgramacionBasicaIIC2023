import helpers
import getpass
import os

arrayTipoCambio = helpers.tipoDeCambio()


# >>> Consultar saldo actual
def getMoneyPath(id):
    return f"users/{id}/saldos.txt"


def getMoney(id):
    with open(getMoneyPath(id), "r") as file:
        balance = file.read().strip()
        return float(balance)


# >>> Actualizar Salfo
def updateMoney(id, newBalance):
    with open(getMoneyPath(id), "w") as file:
        file.write(f"{newBalance}")


# >>> Retirar Dinero
def withdrawMoney(id):
    depositAttempts = 0

    balance = getMoney(id)
    print(f"Saldo actual: ${balance}")

    while depositAttempts < 3:
        try:
            amount = float(input("\nIngrese la cantidad que desea retirar: "))
            if amount <= balance:
                newBalance = balance - amount
                updateMoney(id, newBalance)
                print(f"\n>>> Retiro exitoso. Su nuevo saldo es: ${newBalance:.4f}")
                return
            else:
                depositAttempts += 1
                attemptsLeft = 3 - depositAttempts
                print(f">>> Fondos insuficientes. Le quedan {attemptsLeft} intentos.")
                return
        except ValueError:
            print("\n>>> Por favor, ingrese un monto válido.")
    
    if (depositAttempts == 3):
        print(">>> Ha excedido el máximo de intentos para realizar el depósito, volviendo al menú principal...")
        helpers.returnToMainMenu()
    

# >>> Depositar dinero 

# Menú opciones deposito
def printMenuMoneyType(id):

    balance = getMoney(id)
    print(f"\nSaldo actual: ${balance:.4f}")
    print("Depósito:")
    print("1) Colones")
    print("2) Dólares")
    print("3) Bitcoin")


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


# Realizar deposito
def processDeposit(id, moneyType):
    #minMoney = getMinMoney(moneyType)

    depositAttempts = 0
    while depositAttempts < 3:
        depositMoney = float(input(f"Ingrese el monto a depositar: \n>"))
        if(depositMoney > 0):
            try:    
                convertedMoney = convertMoney(depositMoney, moneyType)
                newMoney = getMoney(id) + convertedMoney
                updateMoney(id, newMoney)
                print(f"\n>>> Depósito realizado. Su nuevo saldo es: ${newMoney:.4f}") #El newMoney:.2f se usa para mostrar solo 4 decimales
                return
            except ValueError:
                print("\n>>> Ingrese solo números.")
        else:
            depositAttempts += 1
            attemptsLeft = 3 - depositAttempts
            print(f"\n>>> El monto ingresado no es válido. Le quedan {attemptsLeft} intentos.")
    
    if (depositAttempts == 3):
        print(">>> Ha excedido el máximo de intentos para realizar el depósito, volviendo al menú principal...")
        helpers.returnToMainMenu()


# Función general para el deposito
def depositMoney(id):
    printMenuMoneyType(id)
    moneyType = int(input("Digite el número de opción correspondiente al tipo de moneda que desea depositar: \n> "))

    processDeposit(id, moneyType)


# >>> Eliminar usuario

# Función para eliminar un usuario
def deleteUser(id, pin, name):
    print("Por favor, ingrese su PIN para confirmar la eliminación de su cuenta:")
    userPin = int(getpass.getpass("PIN: "))

    if userPin == pin:
        balance  = getMoney(id)
        if balance == 0:
            confirm = input(f"¿Está seguro de que desea eliminar su cuenta, {name}? \nDigite 'Si' para confirmar: ")
            if confirm == "Si":
                try:
                    """
                    # Eliminar carpeta de usuario
                    userPath = f"users/{id}"
                    os.remove(userPath)
                    """

                    # Eliminar información del usuario en usuarios_pines.txt
                    linesSafe = []
                    with open("usuarios_pines.txt", "r") as file:
                        lines = file.readlines() # Lee todas las líneas del archivo y las almacena en la lista "lines"
                        for i in range(0, len(lines), 3):  # Procesar de a tres líneas (id, nombre, pin)
                            if lines[i].strip() != id:  # Verifica si el id de la línea actual no coincide con el id que se desea eliminar
                                linesSafe.extend(lines[i:i+3]) # Si no coincide, agrega las tres líneas correspondientes al usuario a "linesSafe"

                    with open("usuarios_pines.txt", "w") as file: # Abre el archivo "usuarios_pines.txt" para sobrescribir su contenido
                        for line in linesSafe:
                            file.write(line) # Escribe cada línea en el archivo, reemplazando el contenido original

                    print("¡Su cuenta ha sido eliminada exitosamente!")
                    return True
                except ValueError:
                    print(f"{ValueError}")
        else:
            print("No puede eliminar su cuenta si tiene dinero disponible. Por favor, retire o juegue su saldo antes.")
    else:
        print("El PIN ingresado no coincide. Operación de eliminación cancelada.")
    return
