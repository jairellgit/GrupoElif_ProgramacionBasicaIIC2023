import random


def start():
    showInstructions()

    # amountToBet = getAmountToBet()
    # setAmountToBet(amountToBet)


def showInstructions():
    print("\nInstrucciones Blackjack")
    print("1. El objetivo es sumar los valores de las cartas para acercarse a 21, se se pasa de 21 pierde.")
    print("2. Las cartas con número valen ese número, las cartas J, Q, K valen 10, y el As puede valer 1 u 11, usted decide.")
    print("3. El crupier le dará dos cartas visibles, y él tendrá una carta visible y otra oculta.")
    print("4. Puede pedir carta nueva para ir sumando o decidir terminar su turno.")
    print("5. Para ganar debe sumar 21 con sus cartas o estar más cercano al 21 que el crupier.")
    print("6. Después de repartir las cartas, tiene la opción de doblar su apuesta.")
    print("7. Si obtiene una carta repetida, puede dividir y jugar con dos manos.")


def getAmountToBet():
    amountToBet = getValidAmountFormat()
    # getMinAmountToBet()
    # getPlayerMoney()
    # hasPlayerEnoughMoney(amountToBet, playerMoney)

    return amountToBet


def getValidAmountFormat():
    amountToBet = 0

    while True:
        try:
            amountToBet = int(input("\nIngrese su apuesta: "))
            break
        except ValueError:
            print("\n>>> Sólo se admiten números.")

    return amountToBet
