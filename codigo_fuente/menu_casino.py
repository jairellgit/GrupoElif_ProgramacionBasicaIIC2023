import helpers
import getpass
import os


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
                print(
                    f"\n>>> Retiro exitoso. Su nuevo saldo es: ${newBalance:.4f}")
                return
            else:
                depositAttempts += 1
                attemptsLeft = 3 - depositAttempts
                print(
                    f">>> Fondos insuficientes. Le quedan {attemptsLeft} intentos.")
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


# Realizar deposito
def processDeposit(id, moneyType):
    depositAttempts = 0
    while depositAttempts < 3:
        depositMoney = float(input(f"Ingrese el monto a depositar: \n>"))
        if (depositMoney > 0):
            try:
                convertedMoney = convertMoney(depositMoney, moneyType)
                newMoney = getMoney(id) + convertedMoney
                updateMoney(id, newMoney)
                # El newMoney:.2f se usa para mostrar solo 4 decimales
                print(
                    f"\n>>> Depósito realizado. Su nuevo saldo es: ${newMoney:.4f}")
                return
            except ValueError:
                print("\n>>> Ingrese solo números.")
        else:
            depositAttempts += 1
            attemptsLeft = 3 - depositAttempts
            print(
                f"\n>>> El monto ingresado no es válido. Le quedan {attemptsLeft} intentos.")

    if (depositAttempts == 3):
        print(">>> Ha excedido el máximo de intentos para realizar el depósito, volviendo al menú principal...")
        helpers.returnToMainMenu()


# Función general para el deposito
def depositMoney(id):
    moneyTypeAttempts = 0
    while moneyTypeAttempts < 3:
        printMenuMoneyType(id)
        moneyType = int(input("Digite el número de opción correspondiente al tipo de moneda que desea depositar: \n> "))

        try:
            if(moneyType == 1) or (moneyType == 2) or (moneyType == 3):
                processDeposit(id, moneyType)
                print("\n>>> Ingrese solo números.")
            else:
                moneyTypeAttempts += 1
                attemptsLeft = 3 - moneyTypeAttempts
                print(f"\n>>> La opción ingresada no es válida. Le quedan {attemptsLeft} intentos.")
        except ValueError:
            print("\n>>> Ingrese solo números.")
    
    if (moneyTypeAttempts == 3):
        print(">>> Ha excedido el máximo de intentos para realizar el depósito, volviendo al menú principal...")
        helpers.returnToMainMenu()

    
# >>> Eliminar usuario

def deleteFilesAndFolder(id):
    userFolder = f"users/{id}"
    
    if os.path.exists(userFolder):
        # Eliminar archivos y subcarpetas dentro de la carpeta del usuario
        for item in os.listdir(userFolder):
            item_path = os.path.join(userFolder, item)
            if os.path.isdir(item_path):
                try:
                    os.rmdir(item_path)
                except Exception as error:
                    print(f"Error al eliminar la carpeta {item_path}: {error}")
            else:
                try:
                    os.remove(item_path)
                except Exception as error:
                    print(f"Error al eliminar el archivo {item_path}: {error}")
        
        # Eliminar carpeta del usuario
        try:
            os.rmdir(userFolder)
        except Exception as error:
            print(f"Error al eliminar la carpeta del usuario {id}: {error}")
        
        # Eliminar información del usuario en usuarios_pines.txt
        linesSafe = []
        with open("usuarios_pines.txt", "r") as file:
            lines = file.readlines() # Lee todas las líneas del archivo y las almacena en la lista "lines"
            skip_user = False
            for line in lines:
                if skip_user:  # Saltar líneas asociadas al usuario a eliminar
                    skip_user = False
                    continue
                if line.strip() == id:  # Verifica si la línea actual contiene el ID que se desea eliminar
                    skip_user = True  # Indicar que las próximas líneas deben ser saltadas
                else:
                    linesSafe.append(line) # Si no es el ID a eliminar, agregar la línea a "linesSafe"

        with open("usuarios_pines.txt", "w") as file: # Abre el archivo "usuarios_pines.txt" para sobrescribir su contenido
            for line in linesSafe:
                file.write(line) # Escribe cada línea en el archivo, reemplazando el contenido original
        
        print(f">>> La información del usuario {id} ha sido eliminada exitosamente.")
    else:
        print(f">>> El usuario {id} no existe.")


# Función para eliminar un usuario
def deleteUser(id, pin, name):
    print("Por favor, ingrese su PIN para confirmar la eliminación de su cuenta:")
    userPin = int(getpass.getpass("PIN: "))

    if userPin == pin:
        balance = getMoney(id)
        if balance == 0:
            confirm = input(
                f"¿Está seguro de que desea eliminar su cuenta, {name}? \nDigite 'Si' para confirmar: ")
            if confirm == "Si":
                try:
                    deleteFilesAndFolder(id)
                    return True
                except ValueError:
                    print(f"{ValueError}")
        else:
            print(">>> No puede eliminar su cuenta si tiene dinero disponible. Por favor, retire o juegue su saldo antes.")
    else:
        print(">>> El PIN ingresado no coincide. Operación de eliminación cancelada.")
    return
