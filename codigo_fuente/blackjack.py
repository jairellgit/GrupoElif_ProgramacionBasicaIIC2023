import random
import helpers


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
    arePlayerCardsEqual = playerCards[0] == playerCards[1]
    # if (arePlayerCardsEqual):
    askToDivideCards()  # Para dividir deben ser cartas de igual valor

    checkPlayerBlackjack()
    menu()


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


hasDividedCards = False


def askToDivideCards():
    global hasDividedCards

    print("Obtuvo 2 cartas iguales, ¿Desea dividir?")
    print("1) Sí")
    print("2) No")

    while True:
        option = input(">>> ")

        if isValidDivideCardsOption(option):
            break

        print("\nOpción inválida, reintente...")

    if option == "1":
        hasDividedCards = True
        divideCards()


def isValidDivideCardsOption(option):
    return option == "1" or option == "2"


def divideCards():
    global playerCards

    playerCards = [[playerCards[0]], [playerCards[1]]]


def checkScore(playerHand):
    playerScore = sum(getCardValues(playerHand))
    blackjack = 21

    if playerScore >= blackjack:
        checkBlackjack(playerScore)


def checkBlackjack(playerScore):
    global crupierCards
    global hasDividedCards

    blackjack = 21
    crupierScore = sum(getCardValues(crupierCards))

    print(f"Tu puntuación es de {playerScore}")
    if (playerScore > blackjack):
        print(
            f"\nPuntuación por encima de {blackjack}... Ha perdido su apuesta.")
        # Manejo de dinero, perdió su apuesta
        return helpers.returnToMainMenu()

    while True:
        newCard = getRandomCard("crupier")
        crupierCards.append(newCard)
        print(f"El crupier saca un {newCard}")

        lastCardValue = getCardValues(crupierCards)[-1]
        crupierScore += lastCardValue
        print(f"Puntuación del crupier: {crupierScore}")

        if crupierScore >= playerScore:
            if (playerScore == crupierScore):
                print("\n¡Es un empate! No ganas ni pierdes la apuesta.")
                break

            elif (crupierScore > blackjack):
                print("\n¡Ganaste! El crupier se pasó de 21")
                # ganarApuesta - manejo de dinero
                break

            elif (crupierScore > playerScore):
                print(
                    f"\nPerdiste... El crupier sacó {crupierScore} y tú {playerScore}")
                # perderApuesta - manejo de dinero
                break

            elif (crupierScore < playerScore):
                print(
                    f"\n¡Ganaste! El crupier sacó {crupierScore} y tú {playerScore}")
                # ganarApuesta - manejo de dinero
                break

    return helpers.returnToMainMenu()


def getCardValues(cards):
    values = []
    specialValues = ["J", "Q", "K"]

    for i in range(len(cards)):
        value = cards[i][:2]
        value = value.replace(" ", "")

        if (value in specialValues):
            values.append(10)
            continue

        values.append(int(value))

    return values


# def checkCrupierBlackjack():
#   global crupierCards


def menu():
    printMenu()
    option = getMenuOption()
    handleMenuOption(option)


def printMenu():
    print("\nMenú de juego")
    print("1) Pedir Carta")
    print("2) Deseo parar")
    print("3) Consultar mis Cartas")
    print("4) Consultar carta del Crupier")


def getMenuOption():
    while True:
        option = input(">>> ")
        if isValidMenuOption(option):
            break
        print("Opción inválida, reintente...")

    return option


def isValidMenuOption(option):
    validOptions = ["1", "2", "3", "4"]

    isValidOption = option in validOptions
    return isValidOption


def handleMenuOption(option):
    if option == "1":
        requestNewCard()
    elif option == "2":
        stand()
    elif option == "3":
        printPlayerCards()
    elif option == "4":
        printCrupierCards()


def requestNewCard():
    global hasDividedCards
    global playerCards

    if hasDividedCards:
        playerHand = getHand()
        addNewCardToHand(playerHand)
        checkScore(playerHand)
    else:
        addNewCardToHand(playerCards)
        checkScore(playerHand)

    menu()


def getHand():
    global playerCards

    print("¿A cuál mano desea agregar una nueva carta?")
    print("1) Mano 1")
    print("2) Mano 2")
    option = getHandOption()

    return playerCards[option - 1]


def getHandOption():
    while True:
        option = input(">>> ")

        if isValidHandOption(option):
            break

        print("Opción inválida, reintente...")

    return option


def isValidHandOption(option):
    return option == "1" or option == "2"


def addNewCardToHand(playerHand):
    newCard = getRandomCard("player")
    playerHand.append(newCard)

    print(f"\nHa obtenido un {newCard}")


def stand():
    global hasDividedCards
    global playerCards

    playerScore = sum(getCardValues(playerCards))

    checkBlackjack(playerScore)


def printPlayerCards():
    global hasDividedCards

    print("\nMis cartas")
    if hasDividedCards:
        printTwoHands()
    else:
        printTheOnlyHand()


def printTheOnlyHand():
    global playerCards
    for i in range(len(playerCards)):
        print(playerCards[i])

    menu()


def printTwoHands():
    global playerCards
    for i in range(len(playerCards)):
        print(f"\nCartas de la mano {i + 1}:")
        for j in range(len(playerCards[i])):
            print(playerCards[i][j])

    menu()


def printCrupierCards():
    global crupierCards

    print("\nCartas del Crupier")
    for i in range(len(crupierCards)):
        isFirstCard = i == 0
        if isFirstCard:
            print("La primer carta del crupier está oculta.")
            continue

        print(crupierCards[i])

    menu()
