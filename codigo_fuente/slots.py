import helpers
import getpass
import os
import random
import time
import user_authentication


arrayConfigAvanzada = helpers.confAvanzada()
# El valor predefinido del acumulado del tragamonedas
acumulate = float(arrayConfigAvanzada[3])
# El valor minimo de apuesta que puede hacer el usuario
minBet = float(arrayConfigAvanzada[4])


def start(id, pin, name):
    global userId
    global userPin
    global userName
    global balance

    userId = id
    userPin = pin
    userName = name
    print(f'\nBienvenido al juego "Tragamonedas" {name}, este es un juego de azar y sus instrucciones basicas son las siguientes:\n'
          '1. Selecciona tu apuesta: Antes de comenzar a jugar, debes elegir cuánto dinero estás dispuesto a apostar en cada tirada. \n'
          '2. Introduce el dinero: Debes digitar la cantidad de dinero que quieras apostar, el dinero que apuestes es el que tengas depositado en tu cuenta del casion con anterioridad.\n'
          '3. Tira de la palanca: Una vez que hayas establecido tu apuesta, debes oprimir la tecla "Enter" para empezar\n'
          '4. Espera a que los carretes se muestren: Los carretes van a ir apareciendo y luego se detendrán de manera aleatoria. Cada carrete contiene símbolos diferentes.\n'
          '5. Verifica las combinaciones: Una vez que los carretes se detengan, se verificarán las combinaciones de símbolos. Si los símbolos forman una combinación ganadora según las reglas del juego, ganarás un premio.\n'
          '6. Cobra tus ganancias: Si obtuviste una combinación ganadora, se te otorgará un premio en función de la tabla de pagos del juego y tu apuesta. Tus ganacias se depositarian a tu salario del casino.\n'
          '7. Sigue jugando: Puedes continuar jugando, ajustando tus apuestas y repitiendo los pasos anteriores. Recuerda que el juego es completamente aleatorio, y las probabilidades de ganar pueden depender de la cantidad de veces que juegues.\n\n'
          '-- ¡Buena suerte! :) --')

    # -------- Seccion para traer el saldo actual del usuario y validarlo ----------#
    userPath = f"users/{userId}/saldos.txt"
    with open(userPath, "r") as moneyFile:
        balance, _ = eval(moneyFile.read().strip())

    if (float(balance) < minBet):
        print("Lo sentimos, no cuenta con saldo suficiente para poder realizar una apuesta minima. Regresando al menu principal...")
        user_authentication.menuCasino(id, pin, name)
    else:
        game()


def game():

    currentMoney = 0
    totalAttemptsSlots = 0
    flag = True
    flag2 = True
    figures = ['@', '#', '+', '7']

    global result
    result = []

    while (flag == True):
        print("\nSaldo actual: "+str(getMoney()))

        try:
            while flag2:
                betMoney = float(
                    input("Digite la cantidad de dinero que desea apostar: "))
                if (betMoney < minBet):
                    print(
                        "Lo sentimos, la cantidad minima a apostar es de $10. Inténtelo nuevamente...")
                else:
                    currentMoney = float(getMoney())-betMoney
                    updateMoney(currentMoney)
                    flag2 = False

        except ValueError:
            print("El valor de dinero ingresado es invalido, intentelo de nuevo")

        input("Presione Enter para jalar la palanca e iniciar el juego >>")

        print("Este es el resultado:")

        if (totalAttemptsSlots == 4):
            for i in range(3):
                result.append("@")
                print(" ".join(result))
                time.sleep(1.5)
        elif (totalAttemptsSlots == 9):
            for i in range(3):
                result.append("#")
                print(" ".join(result))
                time.sleep(1.5)
        elif (totalAttemptsSlots == 14):
            for i in range(3):
                result.append("+")
                print(" ".join(result))
                time.sleep(1.5)
        elif (totalAttemptsSlots == 19):
            for i in range(3):
                result.append("7")
                print(" ".join(result))
                time.sleep(1.5)
            totalAttemptsSlots = 0
        else:
            for i in range(3):
                randomFigure = random.choice(figures)
                result.append(randomFigure)
                print(" ".join(result))
                time.sleep(1.5)

        if (result[0] == "@") and (result[1] == "@") and (result[2] == "@"):
            print("¡Recuperas tu dinero apostado!")
            currentMoney = float(getMoney())+betMoney
            updateMoney(currentMoney)
        elif (result[0] == "#") and (result[1] == "#") and (result[2] == "#"):
            print("¡¡Felicidades, haz obtenido el doble!!")
            currentMoney = float(getMoney())+(betMoney*2)
            updateMoney(currentMoney)
        elif (result[0] == "+") and (result[1] == "+") and (result[2] == "+"):
            print("¡¡¡Felicidades, haz ganado el triple de lo invertido!!!")
            currentMoney = float(getMoney())+(betMoney*3)
            updateMoney(currentMoney)
        elif (result[0] == "7") and (result[1] == "7") and (result[2] == "7"):
            print("♦♦♦ FELICIDADES, GANASTE EL ACUMULADO ♦♦♦")
            currentMoney = float(getMoney())+(betMoney*acumulate)
            updateMoney(currentMoney)
        else:
            print("Estuviste muy cerca, vuelve a intentarlo")

        result.clear()
        totalAttemptsSlots += 1
        option = input("¿Desea jugar nuevamente? (S/N): ")

        if (option == "S" or option == "s"):
            flag == True
        else:
            flag == False
            return flag, user_authentication.menuCasino


def updateMoney(money):
    userPath = f"users/{userId}/saldos.txt"
    with open(userPath, "w") as file:
        file.write(f"({money}, True)")


def getMoney():
    userPath = f"users/{userId}/saldos.txt"
    with open(userPath, "r") as moneyFile:
        balance, _ = eval(moneyFile.read().strip())
    return balance
