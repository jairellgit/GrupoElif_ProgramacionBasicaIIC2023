import random


def start():
    showInstructions()

    # amountToBet = getAmountToBet()
    # setAmountToBet(amountToBet)

    play()


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


def play():
    print("\n¡Comienza el juego!")
    assignCards()


playerCards = []
crupierCards = []


def assignCards():
    global playerCards
    global crupierCards

    print("El crupier reparte las cartas...\n")

    assignCardsTurns = 2
    for i in range(assignCardsTurns):
        playerCards.append(getRandomCard("player"))
        print(f"Te ha tocado un {playerCards[i]}")
        crupierCards.append(getRandomCard("crupier"))
        if i == 1:
            print(f"Al crupier le tocó un {crupierCards[i]}")
        else:
            print("La primer carta del crupier esta oculta.")

    # askToDobuleBet
    askToDivideCards()
    checkBlackjack()
    blackjackMenu()


def getRandomCard(user):
    cardValues = ["As", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
    cardTypes = ["Corazones", "Rombos", "Tréboles", "Picas"]

    randomValue = random.randint(0, len(cardValues) - 1)
    cardValue = cardValues[randomValue]
    if (cardValue == "As" and user == "player"):
        cardValue = f"{getAsCardValue()} (As)"
    elif (cardValue == "As" and user == "crupier"):
        asValidValues = ["1", "11"]
        randomAsValidValue = random.randint(0, 1)
        cardValue = f"{asValidValues[randomAsValidValue]} (As)"

    randomType = random.randint(0, len(cardTypes) - 1)
    cardType = cardTypes[randomType]

    cardColor = None
    if ((cardType == "Corazones") or (cardType == "Rombos")):
        cardColor = "Rojo"
    elif ((cardType == "Tréboles") or (cardType == "Picas")):
        cardColor = "Negro"

    randomCard = f"{cardValue} de {cardType} {cardColor}"
    return randomCard


def getAsCardValue():
    print("\nObtuvo un 'As', elija el valor del As: ")
    print("1) Quiero que sea 1")
    print("2) Quiero que sea 11")

    while True:
        option = input(">>> ")

        if isValidAsCardOption(option):
            if option == "1":
                asCardValue = "1"
            else:
                asCardValue = "11"

            break

        print("\nValor del As inválido, reintente...")

    return asCardValue


def isValidAsCardOption(asCardOption):
    return (asCardOption == "1") or (asCardOption == "2")


def askToDobuleBet():
    print("pendiente")


def askToDivideCards():
    print("pendiente")


def checkBlackjack():
    print("pendiente")


def blackjackMenu():
    print("pendiente")
